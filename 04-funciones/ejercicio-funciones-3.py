# Ejercicio 3:
# Crear un diccionario de alumnos (la clave es el nombre del alumno) y cada alumno tendrá las notas de matemáticas,
# lengua e inglés.
# Crear una función que devuelva la nota media de la clase de una asignatura concreta (Ej: get_nota_media(mates))
# Crear una función que devuelva el alumno con la mejor media del curso (Ej: get_mejor_alumno())

alumnos = {
    "pedro": {
        "mates": 10,
        "lengua": 8,
        "ingles": 7,
        # "etica": 4,
    },
    "sara": {
        "mates": 8,
        "lengua": 9,
        "ingles": 9,
    },
    "mike": {
        "mates": 0,
        "lengua": 1,
        "ingles": 4,
        # "etica": 9,
    },
}

for alumno in alumnos:
    print(len(alumnos[alumno]))


def get_nota_media_clase(asignatura):
    suma_notas = 0
    for notas_alumno in alumnos.values():
        suma_notas += notas_alumno[asignatura]

    return suma_notas / len(alumnos)

media_mates = get_nota_media_clase("mates")
print(media_mates)



# def get_nota_media_clase_1(asignatura, **alumnos):
#     print(alumnos)
#
# get_nota_media_clase_1("mates", pedro={"mates": 10}, sara={"mates: 8"}, mike={"mates": 3})

def get_mejor_alumno():
    # alumno_con_mejor_media = None
    alumno_con_mejor_media = {
        "nombre": "",
        "media": -1
    }
    # [(pedro, {"mates": 10,"lengua": 8,"ingles": 7}), (sara, {})...]
    for nombre, notas_alumno in alumnos.items():
        suma_notas = sum(notas_alumno.values())
        datos_alumno = {
            "nombre": nombre,
            "media": round(suma_notas / len(notas_alumno), 2)
        }

        # if not alumno_con_mejor_media:
        #     alumno_con_mejor_media = datos_alumno
        #     continue

        if alumno_con_mejor_media["media"] < datos_alumno["media"]:
            alumno_con_mejor_media = datos_alumno


    return alumno_con_mejor_media

print(get_mejor_alumno())