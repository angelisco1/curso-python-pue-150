import json

class Persona:
    pass

print(type(Persona))

def contar(self):
    self.cuenta += 1

# type(__name__, __bases__, __dict__)
Contador = type("Contador", (), {
    "cuenta": 0,
    "contar": contar
})

MiInt = type("MiInt", (int,), {})

contador = Contador()

print(contador.cuenta)
contador.contar()
contador.contar()
contador.contar()
print(contador.cuenta)

class Contador2:
    # atributo de clase
    cuenta = 0

    def contar(self):
        self.cuenta += 1

contador2 = Contador2()

print(contador2.cuenta)
contador2.contar()
contador2.contar()
contador2.contar()
print(contador2.cuenta)

# ORM
# Validar campos
# Serialización
# ...

print(Contador.__name__)
print(Contador.__bases__)
print(Contador.__dict__)

int(3)

def init(self, cuenta_inicial):
    # Ahora lo estamos añadiendo como atributo de la instancia
    self.cuenta = cuenta_inicial

Contador3 = type("Contador3", (), {
    "__init__": init,
    "contar": contar
})

contador3 = Contador3(5)
contador3.contar()
print(contador3.cuenta)

print(Contador3.__dict__)
print(contador3.__dict__)



class ComandosBot:

    def buscar(self, tema):
        print(f"Buscar información sobre {tema}")



class GestorComandos:
    def __init__(self, gestor):
        self.gestor = gestor


    def agregar_comando(self, nombre_comando, fn_comando):
        if hasattr(self.gestor, nombre_comando):
            return f"El comando {nombre_comando} ya existe"

        setattr(self.gestor, nombre_comando, fn_comando)
        return f"Se ha añadido el comando {nombre_comando}"


    def ejecutar_comando(self, comando, *args):
        if hasattr(self.gestor, comando):
            fn_comando = getattr(self.gestor, comando)
            if callable(fn_comando):
                try:
                    return fn_comando(*args)
                except Exception:
                    return f"Hay un error al ejecutar el comando {comando}"
            return f"El comando {comando} no es una función"
        return f"El comando {comando} no existe"



comandos_bot = ComandosBot()
gestor_del_bot = GestorComandos(comandos_bot)
print(ComandosBot.__dict__)

# lambda params: operacion
# def suma(n1, n2):
#     print("algo")

gestor_del_bot.agregar_comando("sumar", lambda n1, n2: n1 + n2)
tres = gestor_del_bot.ejecutar_comando("sumar", 1, 2)
print(tres)



class Contador4:
    cuenta: int

    def __init__(self, cuenta):
        self.cuenta = cuenta


print(Contador4.__annotations__)

# if isinstance(contador, Contador):
if isinstance(tres, Contador):
    print("Si")
else:
    print("No")


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



class Ingredient(Serializable):
    id: int
    name: str
    price: float

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


tomate = Ingredient(1, "Tomate", 0.3)

d_tomate = tomate.to_dict()
print(d_tomate)
print(type(d_tomate))

j_tomate = tomate.to_json()
print(j_tomate)
print(type(j_tomate))

ing_1 = Ingredient.from_dict(d_tomate)
print(ing_1)

ing_2 = Ingredient.from_dict({"id": "123", "name": "Pepino", "price": "0.45"})
print(ing_2)

ing_3 = Ingredient.from_json(j_tomate)
print(ing_3)

print(type(ing_1))
print(type(ing_2))
print(type(ing_3))


class Persona(Serializable):
    name: str
    edad: int

    def __init__(self, name, edad):
        self.name = name
        self.edad = edad

    def __str__(self):
        return f"Persona(name={self.name}, edad={self.edad})"


angel = Persona.from_json('{"name": "Ángel", "edad": "33"}')
print(angel)
print(type(angel))