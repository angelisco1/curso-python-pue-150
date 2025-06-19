lista_nums = [1, 2, 3, 4, 5]
uno = lista_nums[0]
dos = lista_nums[1]
# ...
cinco = lista_nums[4]

print(lista_nums[0])
print(lista_nums[1])
print(lista_nums[2])
print(lista_nums[3])
print(lista_nums[4])

for num1, num2 in [(1, 2), (3, 4)]:
    print(num1, num2)


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

k_nombre, k_apellidos, k_email = persona
print(k_nombre)

nombre, apellidos, email = persona.values()
print(nombre)




