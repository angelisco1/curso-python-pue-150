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


class Calculadora:
    # def __init__(self, n1, n2):
    #     self.n1 = n1
    #     self.n2 = n2
    #
    # def suma(self):
    #     return self.n1 + self.n2

    def suma(n1, n2):
        return n1 + n2
    suma = staticmethod(suma)

    @staticmethod
    def resta(n1, n2):
        return n1 - n2


# calculadora = Calculadora(1, 2)
# print(calculadora.suma())
# print(calculadora.suma())
# calculadora.n2 = 5
# print(calculadora.suma())

print(Calculadora.suma(1, 2))
print(Calculadora.resta(10, 2))


class CalculadoraConHistorial:
    def __init__(self):
        self.historial = []

    def suma(self, n1, n2):
        self.historial.append({ "n1": n1, "n2": n2, "resultado": n1 + n2 })
        return n1 + n2


calculadora = CalculadoraConHistorial()
calculadora.suma(1, 2)
calculadora.suma(1, 3)
print(calculadora.historial)


class Logger:
    @staticmethod
    def info(msg):
        print(f"[INFO] {msg}")

    @staticmethod
    def warn(msg):
        print(f"[WARN] {msg}")

    @staticmethod
    def error(msg):
        print(f"[ERROR] {msg}")

Logger().warn("Cuidado con esa propiedad que es un string y la estás sumando a un número")
Logger().error("Estás accediendo a la propiedad aaa que no existe")


# Propiedades privadas __prop_privada = 2 -> _NombreClase<nombre_prop_privada> -> _NombreClase__prop_privada

class Persona:
    def __init__(self, nombre, apellido, dni, telefono, edad, personas_de_confianza):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni # -> _Persona__dni
        self.__telefono = telefono # -> _Persona__telefono
        self.edad = edad
        self.personas_de_confianza = personas_de_confianza

    def get_dni(self):
        print("Getter del DNI", self)
        return self.__dni

    def set_dni(self, nuevo_dni):
        print("Setter del DNI")
        self.__dni = nuevo_dni

    dni = property(get_dni, set_dni)

    @property
    def telefono(self):
        print("Getter del teléfono")
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        print("Setter del teléfono")
        self.__telefono = nuevo_telefono

    def __str__(self):
        return (f"Persona: <nombre: {self.nombre}, apellido: {self.apellido}, dni: {self.__dni}, telefono: "
                f"{self.__telefono}>")

    def __repr__(self):
        return (f"Persona: <nombre: {self.nombre}, apellido: {self.apellido}, dni: {self.__dni}, telefono: "
                f"{self.__telefono}>")

    def __eq__(self, otra_persona):
        return self.dni == otra_persona.dni

    def __ne__(self, otra_persona):
        # return self.dni != otra_persona.dni
        return not self.__eq__(otra_persona)

    def __gt__(self, otra_persona):
        return self.edad > otra_persona.edad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

    def __getattribute__(self, item):
        # print(item)
        if item == "no_existe":
            return "No existe esta propiedad"
        elif item == "dni":
            print("Pasa por el DNI")
            dni = object.__getattribute__(self, item)
            dni_oculto = ("*" * 6) + dni[6:]
            return dni_oculto
        else:
            return object.__getattribute__(self, item)

charly = Persona("Charly", "Falco", "00000000T", "+34 666777888", 45, ["mike"])
# print(charly.__dni)
# print(charly.__telefono)

# # print(charly.get_dni())
# print(charly.dni)
# charly.set_dni("00000001U")
# # print(charly.get_dni())
# print(charly.dni)
# print(charly.get_dni())


# Llama al getter
print("A PARTIR DE AQUI")
print(charly.dni)
print(charly.telefono)

# Llama al setter
charly.dni = "00000001U"
charly.telefono = "+34 678901234"

# Llama al getter y al setter
charly.dni += "ABC"
charly.dni = charly.dni + "ABC"


# Name mangling
print(charly._Persona__dni)
# print(charly.__class__.__name__)

print(charly.__dict__)
print(Persona.__dict__)


# Métodos especiales
# __str__
print(charly)

# __repr__
mike = Persona("Mike", "Kozinski", "0000000T", "+34 654654654", 50, [])
lista_personas = [charly, mike]
print(lista_personas)

sara = Persona("Sara", "Fernández", "0000000T", "+34 654654655", 48,[])

# __eq__
print(mike == charly)
# __ne__
print(mike != charly)

# Como tienen el mismo DNI esto es False
print(mike != sara)

# __gt__
print(mike > charly)
print(charly > sara)

# __lt__
print(charly < sara)

print(charly.no_existe)

