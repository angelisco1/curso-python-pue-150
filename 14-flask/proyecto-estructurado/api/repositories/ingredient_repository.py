import csv

CSV_PATH = "api/data/ingredient.csv"

class IngredientCSVRepository:


    def get_all(self):
        ingredients = []

        try:
            with open(CSV_PATH, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    ingredient = {
                        "id": int(row["id"]),
                        "name": row["name"],
                        "price": float(row["price"]),
                    }
                    ingredients.append(ingredient)
        except FileNotFoundError:
            print("No existe el CSV con los datos")

        return ingredients


    # EJERCICIO: rellenar este método para que lo use el servicio. Tiene que devolver 1 ingrediente o None si no lo
    #  encuentra
    def get_by_id(self):
        pass


    def create(self, ingredient):
        ingredients = self.get_all()
        ingredients.append(ingredient)
        self.__save_ingredients(ingredients)
        return ingredient


    def update(self, id, ingredient_data):
        ingredients = self.get_all()
        for i, ingredient in enumerate(ingredients):
            if ingredient["id"] != id:
                continue

            name, price = ingredient_data.values()
            ingredients[i]["name"] = name
            ingredients[i]["price"] = price
            self.__save_ingredients(ingredients)
            return ingredients[i]

        return None


    def partial_update(self, id, ingredient_data):
        ingredients = self.get_all()
        for i, ingredient in enumerate(ingredients):
            if ingredient["id"] != id:
                continue

            if "price" in ingredient_data:
                ingredients[i]["price"] = ingredient_data["price"]

            if "name" in ingredient_data:
                ingredients[i]["name"] = ingredient_data["name"]

            self.__save_ingredients(ingredients)
            return ingredients[i]

        return None


    # EJERCICIO: rellenar este método para que lo use el servicio. Tiene que eliminar 1 ingrediente y devolver True
    #  si lo ha eliminado y False si no lo ha eliminado
    def delete(self):
        pass


    def __save_ingredients(self, ingredients):
        with open(CSV_PATH, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "price"])
            writer.writeheader()

            for ing in ingredients:
                writer.writerow(ing)