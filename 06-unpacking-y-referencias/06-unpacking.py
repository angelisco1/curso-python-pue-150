lista_nums = [1, 2, 3, 4, 5]
print(lista_nums[0])
print(lista_nums[1])
print(lista_nums[2])
print(lista_nums[3])
print(lista_nums[4])


uno, dos, tres, cuatro, cinco = lista_nums
print(uno)
print(cuatro)

# Da un error porque no estamos desempacando todos los valores
# uno, dos, tres = lista_nums

uno, dos, tres, *resto = lista_nums
print(resto)

uno, dos, tres, *_ = lista_nums
print(_)

*_, cuatro, cinco = lista_nums
print(_)
print(cuatro)
print(cinco)

uno, *_, cinco = lista_nums
print(uno)
print(cinco)


uno, dos = lista_nums[:2]
print(uno)
print(dos)

# [1, 2, 3, 4, 5]
# uno, *_, tres, *a = lista_nums

print(lista_nums)


persona = {
    "nombre": "Charly",
    "apellidos": "Falco",
    "email": "cfalco@gmail.com"
}

nombre, apellidos, email = persona.values()
print(nombre)




