import random
from ..models import Ingredient

# from ..repositories import IngredientCSVRepository, IngredientSQLiteRepository
from ..interfaces import IngredientRepository

# ingredients = [
#     { "id": 1, "name": "Pimiento verde", "price": 0.35 },
#     { "id": 2, "name": "Pimiento rojo", "price": 0.45 },
#     { "id": 3, "name": "Cebolla", "price": 0.5 },
# ]

# ingredient_repository = IngredientCSVRepository()
# ingredient_repository = IngredientSQLiteRepository()


class IngredientService:

    def __init__(self, repository: IngredientRepository):
        self.__ingredient_repository = repository


    def get_ingredients(self):
        # ingredients = self.__ingredient_repository.get_all()
        ingredients = Ingredient.all()
        # print(ingredients)

        return ingredients


    def create_ingredient(self, ingredient):
        # ingredient["id"] = len(ingredients) + 1
        # ingredients.append(ingredient)
        # created_ingredient = self.__ingredient_repository.create(ingredient)
        new_ingredient = Ingredient(name=ingredient.name, price=ingredient.price)
        created_ingredient = new_ingredient.save()

        # ing = Ingredient(**ingredient)
        # ing.save()

        return created_ingredient


    def get_ingredient(self, id):
        # ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        ingredient = self.__ingredient_repository.get_by_id(id)
        return ingredient


    def update_ingredient(self, id, ingredient_data):
        # updated_ingredient = None

        # for i, ing in enumerate(ingredients):
        #     if ing["id"] != id:
        #         continue
        #
        #     ingredient_data["id"] = id
        #     ingredients[i] = ingredient_data
        #     updated_ingredient = ingredients[i]
        updated_ingredient = self.__ingredient_repository.update(id, ingredient_data)

        return updated_ingredient

    def partial_update_ingredient(self, id, ingredient_data):
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
        updated_ingredient = self.__ingredient_repository.partial_update(id, ingredient_data)

        return updated_ingredient


    def delete_ingredient(self, id):
        # global ingredients
        #
        # ingredient = next((ingredient for ingredient in ingredients if ingredient["id"] == id), None)
        # if not ingredient:
        #     return False
        #
        # ingredients = [ingredient for ingredient in ingredients if ingredient["id"] != id]
        # return True
        return self.__ingredient_repository.delete(id)
