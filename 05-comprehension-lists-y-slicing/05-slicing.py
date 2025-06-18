texto = "hola mundo"
hola = texto[0:4]
# hola = texto[:4]
mundo = texto[5:10]
print(hola)
print(mundo)

# Si queremos ir hasta el final, sin poner el índice, podemos dejarlo vacío
mundo = texto[5:]
print(mundo)

# [start:stop:step]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[::2])
print(numeros[1::2])

# i = 0
# i = 2
# i = 4
# i = 6


print(texto[::-2])
print(texto[1::-2])

# -1 -> 9
# 7
# 5
# 3
print(texto)
print(numeros)