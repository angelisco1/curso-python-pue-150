# Ejercicio 2:
# Un usuario introduce un número (oculto)
numero_adivinar = getpass.getpass("Introduce un número para que otro usuario lo intente adivinar: ")

# Le da una pista al siguiente usuario: la longitud del número es: <rellenar esto>
longitud = len(numero_adivinar)
# print("Pista: el número tiene " + str(longitud))
print(f"Pista: el número tiene {longitud} dígitos")

# Otro usuario tiene que adivinar el número (introduce el número que piensa que es)
numero_del_usuario = input("Introduce el número: ")

# Mostrar True si lo ha acertado o False si no lo ha acertado
print(f"Has adivinado el número? {numero_adivinar == numero_del_usuario}")