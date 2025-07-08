file = open("archivos/archivo1.txt", "r")
contenido = file.read()
print(contenido)
file.close()


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


with open("archivos/archivo1.txt", "r") as file:
    lineas = file.readlines()
    for i, linea in enumerate(lineas):
        print(f"Nº linea {i + 1}: {linea}")


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
