from flask import Blueprint, jsonify, make_response, request
from ..repositories import IngredientCSVRepository, IngredientSQLiteRepository
from ..services import IngredientService

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
def get_ingredients():
    ingredients = ingredient_service.get_ingredients()
    return jsonify(ingredients)


@ingredients_bp.route("/ingredients", methods=["POST"])
def post_ingredients():
    ingredient_data = request.json
    ingredient = ingredient_service.create_ingredient(ingredient_data)
    return jsonify(ingredient), 201, {"X-Custom-Header": "patata"}


@ingredients_bp.route("/ingredients/<int:id>")
def get_ingredient_by_id(id):
    ingredient = ingredient_service.get_ingredient(id)
    if not ingredient:
        return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404
    return jsonify(ingredient)


@ingredients_bp.route("/ingredients/<int:id>", methods=["PUT"])
def put_ingredient(id):
    ingredient = request.json

    updated_ingredient = ingredient_service.update_ingredient(id, ingredient)

    if not updated_ingredient:
        return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404

    response = make_response(updated_ingredient)
    # response.status_code = 200
    # response.headers = {}
    return response


@ingredients_bp.route("/ingredients/<int:id>", methods=["PATCH"])
def patch_ingredient(id):
    ingredient_data = request.json

    updated_ingredient = ingredient_service.partial_update_ingredient(id, ingredient_data)
    if not updated_ingredient:
        return jsonify({"message": f"No hemos encontrado el ingrediente con el id {id}"}), 404

    response = make_response(updated_ingredient)
    return response


@ingredients_bp.route("/ingredients/<int:id>", methods=["DELETE"])
def delete_ingredient(id):

    deleted = ingredient_service.delete_ingredient(id)

    if not deleted:
        return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404

    return jsonify(None), 204
