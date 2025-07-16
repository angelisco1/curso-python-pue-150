from abc import ABC, abstractmethod


class IngredientRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def create(self, ingredient):
        pass

    @abstractmethod
    def update(self, id, ingredient_data):
        pass

    @abstractmethod
    def partial_update(self, id, ingredient_data):
        pass

    @abstractmethod
    def delete(self, id):
        pass