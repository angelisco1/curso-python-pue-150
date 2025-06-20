# Ejercicio 1:
# Crear una lista de diccionarios que representan los sugus, y recorrerla mostrando la relación entre sabor y color
# de cada sugus
# azul -> piña
# rojo -> fresa
# ...

lista_sugus = [
    { "sabor": "fresa", "color": "rojo" },
    { "sabor": "piña", "color": "azul" },
    { "sabor": "limón", "color": "amarillo" },
    { "sabor": "naranja", "color": "naranja" },
]

for sugus in lista_sugus:
    # tupla_sugus = sugus.values()
    # print(f"{tupla_sugus[0]} -> {tupla_sugus[1]}")
    print(f"{sugus["color"]} -> {sugus["sabor"]}")

    sabor, color = sugus.values()
    print(f"{color} -> {sabor}")


sugus = {
    "fresa": "rojo",
    "piña": "azul",
    "limón": "amarillo",
    "naranja": "naranja"
}

for sabor, color in sugus.items():
    # (fresa, rojo)
    print(f"{color} -> {sabor}")

