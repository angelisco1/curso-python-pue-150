import csv


with open("archivos/ingredientes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    for linea in reader:
        print(linea)


with open("archivos/ingredientes.csv", "r") as csvfile:
    # reader = csv.DictReader(csvfile, delimiter=",")
    reader = csv.DictReader(csvfile)

    for linea in reader:
        print(linea)


lista_personas = [
    { "id": 1, "nombre": "Charly", "apellidos": "Falco", "puesto": "Desarrollador" },
    { "id": 2, "nombre": "Mike", "apellidos": "Kozinski", "puesto": "Ventas" },
    { "id": 3, "nombre": "Ana", "apellidos": "Fernández", "puesto": "Marketing" },
    { "id": 4, "nombre": "Octavia", "apellidos": "Blake", "puesto": "Desarrollador" },
    { "id": 5, "nombre": "Andrés", "apellidos": "García", "puesto": "Marketing" },
]

with open("archivos/emails_trabajadores.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(("id", "nombre_completo", "email"))

    for trabajador in lista_personas:
        nombre_completo = f"{trabajador["nombre"]} {trabajador["apellidos"]}"
        email = f"{trabajador["nombre"][:1].lower()}.{trabajador["apellidos"].lower()}@loquesea.com"
        writer.writerow((trabajador["id"], nombre_completo, email))


with open("archivos/desarrolladores.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "nombre", "apellidos"])
    writer.writeheader()

    desarrolladores = [{"id": trabajador["id"], "nombre": trabajador["nombre"], "apellidos": trabajador["apellidos"]}
                       for trabajador in lista_personas if trabajador["puesto"] == "Desarrollador"]

    for trabajador in desarrolladores:
        writer.writerow(trabajador)


try:
    with open("archivos/no-existe.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("No existe este archivo")