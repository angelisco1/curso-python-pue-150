import json
from flask import Blueprint, jsonify, make_response, request
from werkzeug.exceptions import NotFound, abort, BadRequest
from ..repositories import IngredientCSVRepository, IngredientSQLiteRepository
from ..services import IngredientService
from ..utils import validate_token, log, serialize, Serializable

ingredients_bp = Blueprint("ingredients", __name__)

# ingredients = [
#     { "id": 1, "name": "Pimiento verde", "price": 0.25 },
#     { "id": 2, "name": "Pimiento rojo", "price": 0.25 },
#     { "id": 3, "name": "Cebolla", "price": 0.35 },
# ]


# ingredient_repository = IngredientCSVRepository()
ingredient_repository = IngredientSQLiteRepository()
ingredient_service = IngredientService(ingredient_repository)


@ingredients_bp.route("/ingredients", methods=["GET"])
@log
def get_ingredients():
    ingredients = ingredient_service.get_ingredients()
    serializados = []
    for ing in ingredients:
        serializados.append(ing.to_dict())
    return jsonify(serializados)


class PostRequestBody(Serializable):
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"PRB(name={self.name}, price={self.price})"


@ingredients_bp.route("/ingredients", methods=["POST"])
@log
# @validate_token
@serialize(PostRequestBody)
def post_ingredients():
    ingredient_data = request.json

    print(f"BODY: {request.body}")
    ingredient_data = request.body

    print(request.headers)

    # if not ("name" in ingredient_data and "price" in ingredient_data):
    if not (hasattr(ingredient_data, "name") and hasattr(ingredient_data, "price")):
        raise BadRequest(f"Tienes que enviar los campos name y price")

    ingredient = ingredient_service.create_ingredient(ingredient_data)
    return jsonify(ingredient.to_dict()), 201, {"X-Custom-Header": "patata"}


@ingredients_bp.route("/ingredients/<int:id>")
@log
def get_ingredient_by_id(id):
    ingredient = ingredient_service.get_ingredient(id)
    if not ingredient:
        # return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404
        # abort(404, description=f"No hemos encontrado el ingrediente con el id {id}")
        raise NotFound(f"No hemos encontrado el ingrediente con el id {id}")
    return jsonify(ingredient)


@ingredients_bp.route("/ingredients/<int:id>", methods=["PUT"])
# @validate_token
def put_ingredient(id):
    ingredient = request.json

    if not ("name" in ingredient and "price" in ingredient):
        raise BadRequest(f"Tienes que enviar los campos name y price")

    updated_ingredient = ingredient_service.update_ingredient(id, ingredient)

    if not updated_ingredient:
        # return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404
        abort(404, description=f"No hemos encontrado el ingrediente con el id {id}")

    response = make_response(updated_ingredient)
    # response.status_code = 200
    # response.headers = {}
    return response


@ingredients_bp.route("/ingredients/<int:id>", methods=["PATCH"])
# @validate_token
def patch_ingredient(id):
    ingredient_data = request.json

    updated_ingredient = ingredient_service.partial_update_ingredient(id, ingredient_data)
    if not updated_ingredient:
        # return jsonify({"message": f"No hemos encontrado el ingrediente con el id {id}"}), 404
        abort(404, description=f"No hemos encontrado el ingrediente con el id {id}")

    response = make_response(updated_ingredient)
    return response


@ingredients_bp.route("/ingredients/<int:id>", methods=["DELETE"])
# @validate_token
def delete_ingredient(id):

    deleted = ingredient_service.delete_ingredient(id)

    if not deleted:
        # return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404
        abort(404, description=f"No hemos encontrado el ingrediente con el id {id}")

    return jsonify(None), 204

