# EJERCICIO 1: Mostrar el siguiente texto por consola
# Se ha iterado 1 vez
# Se ha iterado 2 veces
# Se ha iterado 3 veces
# Se ha iterado 4 veces
# Se ha iterado 5 veces
# Ya hemos terminado de iterar

i = 0
while i < 5:
    if i == 0:
        print(f"Se ha iterado {i + 1} vez")
    else:
        print(f"Se ha iterado {i + 1} veces")
    # i = i + 1
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 1:
        print(f"Se ha iterado {i} vez")
    else:
        print(f"Se ha iterado {i} veces")

print("Ya hemos terminado de iterar")

i = 0
while i < 5:
    match i:
        case 0:
            print(f"Se ha iterado {i + 1} vez")
        case _:
            print(f"Se ha iterado {i + 1} veces")
    i += 1

print("Ya hemos terminado de iterar")

i = 1
vez = "vez"
while i < 5:
    if i == 2:
        vez = "veces"
    print(f"se ha iterado {i} {vez}")
    i += 1

print("Ya hemos terminado de iterar")

i = 0
while i < 5:
    print(f"Se ha iterado {i + 1} {'vez' if i == 0 else 'veces'}")
    i += 1

print("Ya hemos terminado de iterar")