print("Hola mundo!")

print(8 / 3) # En Python 2 el resultado sería un 2
print(8 // 3)
print(2 ** 4)

print("hola mundo" == "HOLA MUNDO")

print(1 == 1 and 2 == 2 and 0 == 0)
print(1 == 1 and 3 == 2)
print(1 == 1 or 3 == 2)
print(1 == 2 or 3 == 2)

print(not True)
print(not False)

print(bin(1001 & 1101))

print("a" in "Hola mundo!")

###############
## Variables ##
###############

nombre = "Charly"
suma = 1 + 2.0

print(nombre)
print(suma)
print(type(suma))

suma = "tres coma cero"
print(suma)
print(type(suma))

# int(suma)

# Constante
PI = 3.14

un_2 = 2
_ = 1

Número = "Número"
print(Número)
print(len(Número))

mi_nombre = "Ángel"
miNombre = "Ángel"


mi_nombre += "!"
# mi_nombre = mi_nombre + "!"
print(mi_nombre)

x, y = 1, 2
print(x)
print(y)

temp = x
x = y
y = temp

x, y = y, x
print(x)
print(y)

####################
## Operaciones IO ##
####################

# nombre = input("Nombre: ")
# apellidos = input("Apellidos: ")
# email = input("Email: ")
# print("Me llamo " + nombre + " " + apellidos + " y si quieres me contactas a " + email)
# print("Me llamo", nombre, apellidos, "y si quieres me contactas a", email)
#
# print(nombre, apellidos, email, sep="-", end=".\n")
# print(nombre, apellidos, email, sep=", ")



#############
## Números ##
#############

print(int(2.4))
print(float("5.2"))
print(float(9))
print(complex(9))
print(str(2.9))

print(int(2.6))
print(round(2.69832478234, 3))
print(max(3, 8, 9, 4, 0))
print(sum([3, 8, 9, 4, 0], 20))


#############
## Strings ##
#############


texto1 = "Hola\n\t\"mundo\""
texto2 = '\'Mundo\'\nhola'

texto3 = """Hola
    mundo"""
# docstring

print(texto1)
print(texto2)
print(texto3)

print(texto1[2])
print(texto1[-1])
# texto1[2] = "7"

print(len(texto3))

nombre = input("Nombre: ")
print("-> " + nombre)
print(len(nombre.strip()) == 0)

email = input("Email: ")
es_de_empresa = not email.endswith("gmail.com")
print("Este email es de empresa?: " + str(es_de_empresa))

print(email.split("@"))

introduccion = input("Introducción: ")
print(introduccion.split(" "))