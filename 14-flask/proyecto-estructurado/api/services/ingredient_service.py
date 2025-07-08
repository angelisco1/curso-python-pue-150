from turtledemo.sorting_animate import start_isort

ingredients = [
    { "id": 1, "name": "Pimiento verde", "price": 0.35 },
    { "id": 2, "name": "Pimiento rojo", "price": 0.45 },
    { "id": 3, "name": "Cebolla", "price": 0.5 },
]


class IngredientService:

    @staticmethod
    def get_ingredients():
        return ingredients

    @staticmethod
    def create_ingredient(ingredient):
        ingredient["id"] = len(ingredients) + 1
        ingredients.append(ingredient)

        return ingredient

    @staticmethod
    def get_ingredient(id):
        ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        return ingredient

    @staticmethod
    def update_ingredient(id, ingredient_data):
        updated_ingredient = None

        for i, ing in enumerate(ingredients):
            if ing["id"] != id:
                continue

            ingredient_data["id"] = id
            ingredients[i] = ingredient_data
            updated_ingredient = ingredients[i]

        return updated_ingredient

    @staticmethod
    def partial_update_ingredient(id, ingredient_data):
        updated_ingredient = None

        for i, ing in enumerate(ingredients):
            if ing["id"] != id:
                continue

            if "price" in ingredient_data:
                ingredients[i]["price"] = ingredient_data["price"]

            if "name" in ingredient_data:
                ingredients[i]["name"] = ingredient_data["name"]

            updated_ingredient = ingredients[i]

        return updated_ingredient

    @staticmethod
    def delete_ingredient(id):
        global ingredients

        ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        if not ingredient:
            return False

        ingredients = [ingredient for ingredient in ingredients if ingredient["id"] != id]
        return True
