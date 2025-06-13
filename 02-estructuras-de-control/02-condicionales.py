nota = 20

if nota < 5:
    print("Ponte las pilas")
elif nota < 7:
    print("Venga, que tu puedes, intenta mejorar un poco más")
elif nota < 9:
    print("Vas muy bien")
elif nota < 10:
    print("Increible, mantén ese nivel")
else:
    print("Qué nota es esa?")


if nota < 5:
    print("Ponte las pilas")
elif nota == 5 or nota <= 10:
# elif nota <= 10:
    print("Sigue así")
else:
    print("Qué nota es esa?")


# if (nota < 5) {
#     print("Ponte las pilas")
# } else if (nota == 5 or nota <= 10) {
#     print("Sigue así")
# } else {
#     print("Qué nota es esa?")
# }

passwords_inseguras = ["1234", "qwerty", "password", "batman"]
password = "12345"
if password in passwords_inseguras:
    print("Cambia la contraseña!!!")


# OPERADOR TERNARIO -> condicion ? codigo del if : codigo del else
mensaje = "Tu contraseña está a salvo" if not password in passwords_inseguras else "Cambia la contraseña!!!"
print(mensaje)


## MATCH (SWITCH - CASE)

nota = 5

match nota:
    case 1:
        print("Ponte las pilas")
    case 2:
        print("Ponte las pilas")
    case 3:
        print("Ponte las pilas")
    case 4:
        print("Ponte las pilas")
    case 5:
        print("Venga, que tu puedes, intenta mejorar un poco más")
    case 6:
        print("Venga, que tu puedes, intenta mejorar un poco más")
    case 7:
        print("Vas muy bien")
    case 8:
        print("Vas muy bien")
    case 9:
        print("Increible, mantén ese nivel")
    case 10:
        print("Increible, mantén ese nivel")
    case _:
        print("Qué nota es esa?")


match nota:
    case n if n < 5:
        print("Ponte las pilas")
    case n if n < 7:
        print("Venga, que tu puedes, intenta mejorar un poco más")
    case n if n < 9:
        print("Vas muy bien")
    case n if n <= 10:
        print("Increible, mantén ese nivel")
    case _:
        print("Qué nota es esa?")


# mensaje_api = { "ErrorMsg": "Noexiste is not a Digimon in our database." }
# mensaje_api = { "ErrorMsg": "No hay conexión." }
mensaje_api = { "name": "Greymon", "img": "https://digimon.shadowsmith.com/img/greymon.jpg", "level": "Champion" }

match mensaje_api:
    case { "ErrorMsg": msg } if msg in ("No hay conexión", "No estás autorizado"):
        print(f"Hay algún error con la API, revisalo: {msg}")
    case { "ErrorMsg": msg }:
        print(f"Hay algún error con la BBDD, revisalo: {msg}")
    case { "name": name, "img": img, "level": level }:
        print(f"{name} ({level}) -> Ver en {img}")


