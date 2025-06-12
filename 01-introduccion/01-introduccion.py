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
print(x)
print(y)

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
texto4 = 'Hola\n\t"mundo"'

texto3 = """Hola
    mundo"""
# docstring

print(texto1)
print(texto2)
print(texto3)

print(texto1[2])
print(texto1[-1])

texto5 = "Ángel"

print(texto5[len(texto5) - 1])
print(texto5[-1])
# texto1[2] = "7"

print(len(texto3))

# nombre = input("Nombre: ")
# print("-> " + nombre)
# print(len(nombre.strip()) == 0)
#
# email = input("Email: ")
# es_de_empresa = not email.endswith("gmail.com")
# print("Este email es de empresa?: " + str(es_de_empresa))
#
# print(email.split("@"))



introduccion = input("Introducción: ")
introduccion_separada = introduccion.split(" ")
print(introduccion_separada)

introduccion_por_comas = ", ".join(introduccion_separada)
print(introduccion_por_comas)

producto_1 = "1,patatas,2000,1.50,murcia"
datos_producto = producto_1.split(",")
print("Nombre: " + datos_producto[1].title())
print("Cantidad: " + datos_producto[2])

###################
## FORMATEADORES ##
###################

print('Mi color favorito es: %X' % 16431834)

precio1 = 3.95
precio2 = 400.52783
precio3 = 99.99

print("Precio producto 1: %f€" % precio1)
print("Precio producto 2: %f€" % precio2)
print("Precio producto 3: %f€" % precio3)

print("Precio producto 1: %10.2f€" % precio1)
print("Precio producto 2: %10.2f€" % precio2)
print("Precio producto 3: %10.2f€" % precio3)

print("Precio producto 2: {}€".format(precio2))


ganancias_potenciales = int(datos_producto[2]) * float(datos_producto[3])

print(
    "El producto {0} (de {3}) tiene un precio de {2}€ y en el almacén tenemos {1} unidades. Ganancias potenciales: {1:>10} x {2}€ = {4}".format(
        datos_producto[1].title(),
        datos_producto[2],
        datos_producto[3],
        datos_producto[4],
        ganancias_potenciales
    )
)

print(
    "El producto {nombre} (de {origen}) tiene un precio de {precio}€ y en el almacén tenemos {cantidad} unidades. Ganancias potenciales: {cantidad:>10} x {precio}€ = {ganancias}".format(
        nombre=datos_producto[1].title(),
        cantidad=datos_producto[2],
        precio=datos_producto[3],
        origen=datos_producto[4],
        ganancias=ganancias_potenciales
    )
)

# f-strings

print(f"""
Producto: {datos_producto[1].title()} (de {datos_producto[4]})
Precio: {datos_producto[3]}€
Stock: {datos_producto[2]} unidades
Ganancias potenciales: {datos_producto[2]:>10} x {datos_producto[3]}€ = {ganancias_potenciales}
""")

print(f"Producto: {datos_producto[1].title()} (de {datos_producto[4]})")


# El import debería de ir al principio del archivo
import getpass

password = getpass.getpass("Introduce tu contraseña:")
print(password)


print('a' < 'b')
print('a' < 'B')

x = 1
y = 4
# resultado = x <= 2 < y
resultado = x <= 2 and y > 2

ciudadano_eeuu = input("Eres de EEUU? ")
edad = input("Cuantos años tienes? ")
print(f"Puedes conducir?: {ciudadano_eeuu.lower().strip() == 'si' and int(edad) >= 16}")
print(f"Puedes beber alcohol?: {(ciudadano_eeuu.lower().strip() == 'si' and int(edad) >= 21) or (int(edad) >= 18)}")


