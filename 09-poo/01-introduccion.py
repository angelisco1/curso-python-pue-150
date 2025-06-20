# l1 = list([1, 2, 3])
# l1.append(5)

def fn():
    return "Hola"

saludo_fn = fn
print(saludo_fn)
print(fn)

print(fn())
print(saludo_fn())


def usuario(nombre, apellido):
    def get_nombre_completo():
        return f"{nombre} {apellido}"

    return {
        "nombre": nombre,
        "apellido": apellido,
        # "nombre_completo": get_nombre_completo(),
        "get_nombre_completo": get_nombre_completo
    }

angel = usuario("Ángel", "Villalba")
print(angel)
paco = usuario("Paco", "Villalba")
print(paco)
# print(paco["nombre_completo"])
# paco["apellido"] = "Fernández"
# print(paco["nombre_completo"])

print(paco["get_nombre_completo"]())
paco["apellido"] = "Fernández"
print(paco["get_nombre_completo"]())


class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


print(Usuario)

angel = Usuario("Ángel", "Villalba")
print(angel.nombre)
print(angel.apellido)

paco = Usuario("Paco", "García")
print(paco.nombre)
print(paco.apellido)

print(angel.get_nombre_completo())
print(paco.get_nombre_completo())
paco.apellido = "Fernández"
print(paco.get_nombre_completo())

# Esta manera de llamar al método no es la correcta
# print(Usuario.get_nombre_completo(angel))


class Usuario2:
    
    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]


paco = Usuario2({"nombre": "Paco", "apellido": "García", "edad": 39})


class Usuario3:
    pass


s = Usuario3()
s.nombre = "Charly"
print(s.nombre)


class Coche:
    num_ruedas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # self.num_ruedas = 4


seat_ibiza = Coche("Seat", "Ibiza")
print(seat_ibiza.num_ruedas)
seat_ibiza.num_ruedas = 3
print(seat_ibiza.num_ruedas)

print(Coche.num_ruedas)


