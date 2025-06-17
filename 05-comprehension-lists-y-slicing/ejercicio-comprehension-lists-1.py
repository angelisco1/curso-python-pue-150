# Ejercicio 1:
# Dada una lista con grados centigrados ([16, 21, 25, 27, 32, 30, 28, 29])
# Obtener la lista con los grados fahrenheit
# Y otra lista con los grados kelvin

# tupla_grados = (16, 21, 25, 27, 32, 30, 28, 29)
# tupla_grados[2] = 23

# set_grados = {16, 27, 25, 27, 32, 30, 28, 29}

grados = [16, 21, 25, 27, 32, 30, 28, 29]
grados[2] = 23

grados_kelvin = [grado + 273.15 for grado in grados]
grados_fahrenheit = [round((grado * 9 / 5) + 32, 2) for grado in grados]

print(grados_kelvin)
print(grados_fahrenheit)