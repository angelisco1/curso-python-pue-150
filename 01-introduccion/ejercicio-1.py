# Ejercicio 1: upper, operadores
# input("Introduce un texto: ")
# print(True | False)

texto = input("Introduce un texto: ")

texto_mayusculas = texto.upper()
print("El texto está en mayúsculas?", texto_mayusculas == texto)
# "HOLA" == "hola" -> FALSE
# "HOLA" == "HOLA" -> TRUE
# "HOLA" == "hOlA" -> FALSE

# Otra solución
print("El texto está en mayúsculas?", texto.isupper())