# Ejercicio 1:
# Pedir a un usuario números de uno en uno para sumarlos
# La suma hay que hacerla cuando el usuario ya no quiere introducir más números
# El usuario decide no introducir más números cuando introduce el texto "terminar"

# bucles, listas, condicionales

print("abc".isalpha())
print("123".isalpha())
print("1adas23".isalpha())
print("FA0".isalnum())
print("#FA0".isdigit())

# print(int("12b"))
print(hex(123))
print(int(0x7b))
# a = "0x"+"7b"
# print(int(a))
print(int('0x123B', 16))


lista_nums = []
while True:
    num = input("Introduce un número para sumar (escribe 'terminar' para mostrar la suma): ")
    if num.isalpha() and num.lower() == "terminar":
        break
    lista_nums.append(int(num))

suma_total = sum(lista_nums)
print(f"La suma de los números introducidos ({lista_nums}) es: {suma_total}")
# {", ".join(lista_nums)}


lista_nums = []
suma_total = 0
while True:
    num = input("Introduce un número para sumar (escribe 'terminar' para mostrar la suma): ")
    if num.isalpha() and num.lower() == "terminar":
        break
    lista_nums.append(int(num))
    suma_total += int(num)

print(f"La suma de los números introducidos ({lista_nums}) es: {suma_total}")


lista_nums = []
while True:
    num = input("Introduce un número para sumar (escribe 'terminar' para mostrar la suma): ")
    if num.isalpha() and num.lower() == "terminar":
        break
    lista_nums.append(int(num))

suma_total = 0
for num in lista_nums:
    suma_total += num

print(f"La suma de los números introducidos ({lista_nums}) es: {suma_total}")