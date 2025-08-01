file = open("archivos/archivo1.txt", "r")
contenido = file.read()
print(contenido)
file.close()


# class Open:
#     def __init__(self, ruta, modo):
#         self.file = open(ruta, modo)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self):
#         self.file.close()

# Context managers (with)
with open("archivos/archivo1.txt", "r") as file:
    # Lee el archivo entero
    contenido = file.read()

    # Lee el archivo a trozos (2 bytes)
    # contenido = file.read(2)
    print(contenido)


with open("archivos/archivo1.txt", "r") as file:
    # Lee línea a línea
    contenido = file.readline()
    print(contenido)

    contenido = file.readline()
    print(contenido)


with (open("archivos/archivo1.txt", "r") as file):
    # Lee línea a línea
    contenido = file.readline()
    while contenido:
        print(contenido)
        contenido = file.readline()
    print("Fin del archivo")

# Con el operador morsa := (asigna el valor al mismo tiempo que se comprueba la condición)
with (open("archivos/archivo1.txt", "r") as file):
    # Lee línea a línea
    while contenido := file.readline():
        print(contenido)
    print("Fin del archivo")


with open("archivos/archivo1.txt", "r") as file:
    lineas = file.readlines()
    for i, linea in enumerate(lineas):
        print(f"Nº linea {i + 1}: {linea}")


# Escritura de archivos
# __enter__, __exit__
with open("archivos/archivo_creado.txt", "w") as file:
    file.write("¿Qué le dice un rio a otro?\n")
    file.write("Eh, Bro")


with open("archivos/archivo_creado.txt", "w") as file:
    file.write("Algo más corto\n")


with open("archivos/archivo_creado.txt", "a") as file:
    file.write("Hola mundo")


ingredientes = []

with open("archivos/ingredientes.csv", "r") as file:
    contenido = file.read()
    filas = contenido.split("\n")
    print(len(filas))
    cabeceras, *resto_filas = filas
    print(cabeceras)
    print(resto_filas)
    cab1, cab2, cab3 = cabeceras.split(",")

    for ingrediente_str in resto_filas:
        print(f"- {ingrediente_str}")
        lista_valores = ingrediente_str.split(",")
        id, nombre, precio = lista_valores
        print(id, nombre, precio)
        ingredientes.append({ cab1: id, cab2: nombre, cab3: precio })

print(ingredientes)
