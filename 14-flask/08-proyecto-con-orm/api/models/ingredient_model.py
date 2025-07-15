from ..orm import IntField, StringField, FloatField, Model
from ..utils import Serializable

class Ingredient(Model, Serializable):
    id: int
    name: str
    price: float

    id = IntField(primary_key=True)
    name = StringField()
    price = FloatField()

    def __str__(self):
        return f"Ingredient(id={self.id}, name={self.name}, price={self.price})"

    def __repr__(self):
        return f"Ingredient(id={self.id}, name={self.name}, price={self.price})"