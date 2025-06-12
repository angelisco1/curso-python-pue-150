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


# OPERADOR TERNARIO
mensaje = "Tu contraseña está a salvo" if not password in passwords_inseguras else "Cambia la contraseña!!!"
print(mensaje)