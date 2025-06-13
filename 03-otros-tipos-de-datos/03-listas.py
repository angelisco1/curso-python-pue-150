una_lista = [1, 'abc', 9.36, ['amarillo'], True]
una_lista_vacia = list()

lista_nums = [1, 2, 3, 4]
print(lista_nums[2])

lista_nums[2] = 7
print(lista_nums)

texto = 'hola'
print(list(texto))

lista_nums = list([1, 2, 3, 4, 4, 4, 2, 2, 6, 7, 7, 8])
print(lista_nums)

print(f"El número 7 está {lista_nums.count(7)} veces en la lista")

print(list([texto]))

usuario1 = "Charly"
usuario2 = "Mike"
usuario3 = "Octavia"

usuarios_conectados = []
print(usuarios_conectados)

usuarios_conectados.append(usuario2)
usuarios_conectados.append(usuario3)
print(usuarios_conectados)

usuarios_conectados.append(usuario1)
print(usuarios_conectados)

if usuario2 not in usuarios_conectados:
    usuarios_conectados.append(usuario2)
    print(f"Se ha conectado {usuario2}")
else:
    print(f"El usuario {usuario2} ya estaba conectado")

# match usuario:
#     case { "name": nombre, "rol": "ADMIN" }:
#         HACEMOS ALGO PARA ADMINS
#         LO MOSTRAMOS COMO CONECTADO
#     case { "name": nombre, "rol": "FREE" }:
#         LO MOSTRAMOS COMO CONECTADO

print(usuarios_conectados)


ultimo_usuario = usuarios_conectados.pop()
# penultimo_usuario = usuarios_conectados.pop(-2)

print(ultimo_usuario)
print(usuarios_conectados)


texto_mayus = texto.upper()
print(texto_mayus)
print(texto)

pos_usuario2 = usuarios_conectados.index(usuario2)
print(pos_usuario2)

usuario4 = "Brian"
usuarios_desconectados = ["Sara", usuario4, "Maria", "Brian"]
usuarios_conectados.extend(usuarios_desconectados)
print(usuarios_conectados)

usuarios_conectados.remove("Brian")
print(usuarios_conectados)

usuarios_conectados.insert(3, "Jim")
print(usuarios_conectados)


matriz = [
    [[1, 2, 3], [0, 0, 0], [9, 8, 7]],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])
print(matriz[2][1])
print(matriz[0])
print(matriz[0][2][0])