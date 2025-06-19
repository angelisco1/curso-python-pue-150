json = {
    "nombre": "Json",
    "apellido": "Statham",
    "edad": 50
}

yaml = json
yaml["nombre"] = "Yaml"

print(yaml)
print(json)

num = 3
num2 = num
num2 = 8
print(num)
print(num2)

texto = "hola mundo"
texto2 = texto
texto2 = "adios mundo"
print(texto)
print(texto2)


lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)

tupla1 = (1, 2, 3)
tupla2 = tupla1
print(tupla1)


# Copia/Fusión

lista3 = [*lista1]
lista1.append(5)
lista3.append(10)
print(lista1)
print(lista2)
print(lista3)

toml = {**json}
toml["nombre"] = "Toml"
print(toml)
print(json)
print(yaml)

credenciales_toml = {
    "email": "toml@gmail.com",
    "password": "1234"
}

toml_completo = {**toml, **credenciales_toml, "edad": 40}
print(toml_completo)

lista4 = [12, 13]
lista_nueva = [*lista3, *lista4, 30, 39]
print(lista_nueva)


lista5 = lista4[:]
lista5.append(30)
print(lista5)
print(lista4)