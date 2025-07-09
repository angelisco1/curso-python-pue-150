import random

from ..repositories import IngredientCSVRepository

# ingredients = [
#     { "id": 1, "name": "Pimiento verde", "price": 0.35 },
#     { "id": 2, "name": "Pimiento rojo", "price": 0.45 },
#     { "id": 3, "name": "Cebolla", "price": 0.5 },
# ]

ingredient_repository = IngredientCSVRepository()

class IngredientService:

    @staticmethod
    def get_ingredients():
        ingredients = ingredient_repository.get_all()
        return ingredients


    @staticmethod
    def create_ingredient(ingredient):
        # ingredient["id"] = len(ingredients) + 1
        # ingredients.append(ingredient)
        ingredient["id"] = random.randint(0, 10000)
        created_ingredient = ingredient_repository.create(ingredient)

        return created_ingredient

    @staticmethod
    def get_ingredient(id):
        # ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        ingredient = ingredient_repository.get_by_id(id)
        return ingredient

    @staticmethod
    def update_ingredient(id, ingredient_data):
        # updated_ingredient = None

        # for i, ing in enumerate(ingredients):
        #     if ing["id"] != id:
        #         continue
        #
        #     ingredient_data["id"] = id
        #     ingredients[i] = ingredient_data
        #     updated_ingredient = ingredients[i]
        updated_ingredient = ingredient_repository.update(id, ingredient_data)

        return updated_ingredient

    @staticmethod
    def partial_update_ingredient(id, ingredient_data):
        # updated_ingredient = None
        #
        # for i, ing in enumerate(ingredients):
        #     if ing["id"] != id:
        #         continue
        #
        #     if "price" in ingredient_data:
        #         ingredients[i]["price"] = ingredient_data["price"]
        #
        #     if "name" in ingredient_data:
        #         ingredients[i]["name"] = ingredient_data["name"]
        #
        #     updated_ingredient = ingredients[i]
        updated_ingredient = ingredient_repository.partial_update(id, ingredient_data)

        return updated_ingredient

    @staticmethod
    def delete_ingredient(id):
        # global ingredients
        #
        # ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        # if not ingredient:
        #     return False
        #
        # ingredients = [ingredient for ingredient in ingredients if ingredient["id"] != id]
        # return True
        return ingredient_repository.delete(id)
