num_telefono = {
    "prefijo": "+34",
    "numero": 666777888
}

otro_num_telefono = {
    "prefijo": "+34",
    "numero": 6786786678
}

num_spain = {
    # "prefijo": "+34",
    "numero": 6786786678
}

print(f"Me puedes llamar al número {num_telefono["prefijo"]} {num_telefono["numero"]}")
print(f"Me puedes llamar al número {otro_num_telefono["prefijo"]} {otro_num_telefono["numero"]}")
# print(f"Me puedes llamar al número {num_spain["prefijo"]} {num_spain["numero"]}")
print(f"Me puedes llamar al número {num_spain.get("prefijo", "+45")} {num_spain["numero"]}")

otro_num_telefono["prefijo"] = "+38"
print(f"Me puedes llamar al número {otro_num_telefono["prefijo"]} {otro_num_telefono["numero"]}")

prefijo_num_telf = otro_num_telefono.pop("prefijo")
print(f"Me puedes llamar al número {prefijo_num_telf} {otro_num_telefono["numero"]}")
print(otro_num_telefono)

digimon = {"name":"Koromon","img":"https://digimon.shadowsmith.com/img/koromon.jpg","level":"In Training"}
# digimon.values -> (Koromon, la url, In training)
for val in digimon.values():
    print(val)

# digimon.keys -> (name, img, level)
for key in digimon.keys():
    print(key)

# digimon.items -> ((name, Koromon), (img, la url), (level, In training))
for item in digimon.items():
    print(item)


usuario = {
    "email": "cfalco@gmail.com",
    "password": "1234"
}

apellidos = "Falco"

info_usuario = {
    "nombre": "Charly",
    "apellidos": apellidos,
    "edad": 39,
    "email": "charly@gmail.com"
}

usuario.update(info_usuario)
print(usuario)

