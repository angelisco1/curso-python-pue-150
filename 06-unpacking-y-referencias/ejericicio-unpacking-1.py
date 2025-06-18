import math

equipos1 = ['Valencia', 'Real Madrid', 'Barcelona', 'Sevilla']
# ----
# Barcelona vs Valencia
# Real Madrid vs Sevilla
# ----
# Valencia vs Real Madrid
# Barcelona vs Sevilla

equipos2 = ['Valencia', 'Real Madrid', 'Barcelona', 'Sevilla', 'Ath. Bilbao']
# ----
# Valencia vs Real Madrid
# Barcelona vs Sevilla
# Ath. Bilbao pasa de fase automáticamente

# Enfrentamientos aleatorios (no os lieis con esto)
# Unpacking y */**
# Pista: podéis utilizar funciones recursivas

def get_enfrentamientos_bucle(equipos):
    # a = len(equipos) / 2 if len(equipos) % 2 else (len(equipos) / 2) + 1
    for i in range(math.ceil(len(equipos) / 2)):
        if i*2+2 > len(equipos):
            print(f"{equipos[-1]} pasa automáticamente")
        else:
            equipo1, equipo2 = equipos[i*2:i*2+2]
            print(f"{equipo1} vs {equipo2}")

    print("FIN DE LA TABLA")

get_enfrentamientos_bucle(equipos1)
get_enfrentamientos_bucle(equipos2)

def get_enfrentamientos_rellenando(equipos):
    if len(equipos) % 2:
        equipos.append(None)

    for i in range(0, round(len(equipos)), 2):
        equipo1, equipo2 = equipos[i:i+2]
        if equipo2:
            print(f"{equipo1} vs {equipo2}")
        else:
            print(f"{equipo1} pasa automáticamente")

    print("- FIN DE LA TABLA")

get_enfrentamientos_rellenando(equipos1)
get_enfrentamientos_rellenando(equipos2)


def get_enfrentamientos(equipos):
    if len(equipos) == 0:
        print("Fin de la tabla")
    elif len(equipos) == 1:
        print(f"El {equipos[0]} pasa de fase automáticamente")
        print("Fin de la tabla")
    else:
        # []
        equipo1, equipo2, *resto = equipos
        print(f"{equipo1} vs {equipo2}")
        get_enfrentamientos(resto)


get_enfrentamientos(equipos1)
get_enfrentamientos(equipos2)


# def get_enfrentamientos_list(equipos):
#     enfrentamientos = []
#     if len(equipos) == 0:
#         print("Fin de la tabla")
#     elif len(equipos) == 1:
#         print(f"El {equipos[0]} pasa de fase automáticamente")
#         print("Fin de la tabla")
#     else:
#         equipo1, equipo2, *resto = equipos
#         print(f"{equipo1} vs {equipo2}")
#         get_enfrentamientos(resto)

# enfrentamientos = get_enfrentamientos_list(equipos1)
# print(enfrentamientos)
#
# enfrentamientos2 = get_enfrentamientos_list(equipos2)
# print(enfrentamientos2)