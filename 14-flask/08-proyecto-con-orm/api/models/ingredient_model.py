from ..orm import IntField, StringField, FloatField, Model
import json


class Serializable:
    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__annotations__}

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        print(f"DATA: {data}")
        diccionario = {}
        for attr, tipo in cls.__annotations__.items():
            print(f"{attr} del tipo: {tipo}")
            valor = data.get(attr)

            if tipo == int and isinstance(valor, str) and valor.isdigit():
                diccionario[attr] = int(valor)
            elif tipo == float and isinstance(valor, str):
                diccionario[attr] = float(valor)
            else:
                diccionario[attr] = tipo(valor)


        # Ingredient(id=123, name="Pepino", price=0.45)
        return cls(**diccionario)


    @classmethod
    def from_json(cls, data_json):
        data_dict = json.loads(data_json)
        return cls.from_dict(data_dict)

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