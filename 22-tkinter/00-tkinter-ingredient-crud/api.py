import requests

class IngredientAPI:
    BASE_URL = "http://localhost:3006"

    def get_ingredients(self):
        response = requests.get(f"{self.BASE_URL}/ingredients")
        response.raise_for_status()
        return response.json()

    def get_ingredient(self, id):
        response = requests.get(f"{self.BASE_URL}/ingredients/{id}")
        response.raise_for_status()
        return response.json()

    def delete_ingredient(self, ingredient_id):
        response = requests.delete(f"{self.BASE_URL}/ingredients/{ingredient_id}")
        response.raise_for_status()
        return None

    def create_ingredient(self, name, price):
        data = {
            "name": name,
            "price": price,
        }
        response = requests.post(f"{self.BASE_URL}/ingredients", json=data)
        response.raise_for_status()
        return response.json()

    def update_ingredient(self, id, name, price):
        data = {
            "name": name,
            "price": price,
        }
        print(f"{self.BASE_URL}/ingredients/{id}")
        response = requests.put(f"{self.BASE_URL}/ingredients/{id}", json=data)
        response.raise_for_status()
        return response.json()