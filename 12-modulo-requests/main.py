import requests
from flask import request_started

URL_BASE = "http://localhost:3000"


def get_ingredientes(**kwargs):
    response = requests.get(f"{URL_BASE}/ingredientes", params=kwargs)
    print(response.status_code)
    ingredientes = response.json()

    for ing in ingredientes:
        print(f"{ing["nombre"]} - {ing["precio"]}€")


def get_ingrediente(id):
    response = requests.get(f"{URL_BASE}/ingredientes/{id}")
    print(response.status_code)
    ingrediente = response.json()

    print(f"{ingrediente["nombre"]} - {ingrediente["precio"]}€")


def post_ingrediente(nombre, precio):
    response = requests.post(f"{URL_BASE}/ingredientes", json={"nombre": nombre, "precio": precio})
    print(response.status_code)
    ingrediente_creado = response.json()

    print(ingrediente_creado)


def put_ingrediente(id, nombre, precio):
    response = requests.put(f"{URL_BASE}/ingredientes/{id}", json={"nombre": nombre, "precio": precio})
    # response = requests.put(f"{URL_BASE}/ingredientes/{id}", json={"precio": precio})
    print(response.status_code)

    ingrediente_actualizado = response.json()
    print(ingrediente_actualizado)


def patch_ingrediente(id, nombre, precio):
    # response = requests.patch(f"{URL_BASE}/ingredientes/{id}", json={"nombre": nombre, "precio": precio})
    response = requests.patch(f"{URL_BASE}/ingredientes/{id}", json={"precio": precio})
    print(response.status_code)

    ingrediente_actualizado = response.json()
    print(ingrediente_actualizado)


def delete_ingrediente(id):
    response = requests.delete(f"{URL_BASE}/ingredientes/{id}")
    print(response.status_code)

    # ingrediente_eliminado = response.json()
    # print(ingrediente_eliminado)


# HEAD, OPTIONS, TRACE
# QUERY



# get_ingredientes()
# get_ingrediente(1)
# get_ingrediente(3)
# post_ingrediente("Tomate", 0.4)
# post_ingrediente("Queso mozzarela", 0.38)

# put_ingrediente(5, "Queso mozzarela", 0.45)
# patch_ingrediente(5, "Queso mozzarela", 0.70)

# post_ingrediente("Piña", 0.58)
# delete_ingrediente(8)

get_ingredientes(_sort="precio", _order="asc")
