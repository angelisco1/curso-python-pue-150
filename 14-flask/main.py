from flask import Flask, jsonify, request, make_response

ingredients = [
    { "id": 1, "name": "Pimiento verde", "price": 0.25 },
    { "id": 2, "name": "Pimiento rojo", "price": 0.25 },
    { "id": 3, "name": "Cebolla", "price": 0.35 },
]

app = Flask(__name__)


@app.route("/ingredients", methods=["GET"])
def get_ingredients():
    return jsonify(ingredients)


@app.route("/ingredients", methods=["POST"])
def post_ingredients():
    # data = request.form
    ingredient = request.json
    ingredient["id"] = len(ingredients) + 1
    ingredients.append(ingredient)
    return jsonify(ingredient), 201, {"X-Custom-Header": "patata"}


@app.route("/ingredients/<int:id>")
def get_ingredient_by_id(id):
    ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
    if not ingredient:
        return jsonify({ "message": f"No hemos encontrado el ingrediente con el id {id}" }), 404
    return jsonify(ingredient)


@app.route("/ingredients/<int:id>", methods=["PUT"])
def put_ingredient(id):
    ingredient = request.json
    response = None

    for i, ing in enumerate(ingredients):
        if ing["id"] != id:
            continue
        # ingredients[i]["name"] = ingredient["name"]
        # ingredients[i]["price"] = ingredient["price"]
        ingredient["id"] = id
        ingredients[i] = ingredient

        response = make_response(ingredients[i])
        break

    # response.status_code = 200
    # response.headers = {}
    return response


@app.route("/ingredients/<int:id>", methods=["PATCH"])
def patch_ingredient(id):
    ingredient_data = request.json
    response = None

    for i, ing in enumerate(ingredients):
        if ing["id"] != id:
            continue

        if "price" in ingredient_data:
            ingredients[i]["price"] = ingredient_data["price"]

        if "name" in ingredient_data:
            ingredients[i]["name"] = ingredient_data["name"]

        response = make_response(ingredients[i])
        break

    return response


if __name__ == "__main__":
    app.run(debug=True, port=3006)

