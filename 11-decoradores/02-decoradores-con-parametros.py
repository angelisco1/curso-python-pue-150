import time
import math

# def medir_tiempo_ejecucion(fn_decorada):
#     def wrapper(*args, **kwargs):
#         inicio = time.time()
#         print(f"Inicio: {inicio}")
#
#         resultado = fn_decorada(*args, **kwargs)
#
#         fin = time.time()
#         print(f"Fin: {fin}")
#
#         print(f"La ejecución de la función {fn_decorada.__name__} ha sido de {fin - inicio} segundos")
#         return resultado
#     return wrapper


def medir_tiempo_ejecucion(unidad_de_medida="s", num_decimales=3):
    unidades_de_medidas = {
        "s": 1,
        "ms": 1000
    }

    # Devolvemos el decorador
    def decorador(fn_decorada):
        def wrapper(*args, **kwargs):
            inicio = time.time()
            print(f"Inicio: {inicio}")

            resultado = fn_decorada(*args, **kwargs)

            fin = time.time()
            print(f"Fin: {fin}")
            # entero, decimales = str((fin - inicio) * unidades_de_medidas[unidad_de_medida]).split(".")


            print(f"La ejecución de la función {fn_decorada.__name__} ha sido de "
                  # f"{entero}.{decimales[:num_decimales]}"
                  f"{((fin - inicio) * unidades_de_medidas[unidad_de_medida]):.{num_decimales}f}"
                  f" {unidad_de_medida}")

            return resultado

        return wrapper
    return decorador


@medir_tiempo_ejecucion("ms", 3)
def suma(n1, n2):
    # time.sleep(2)
    return n1 + n2

tres = suma(1, 2)
print(tres)


def suma(n1, n2):
    return n1 + n2


fn_decorador = medir_tiempo_ejecucion("ms", 2)
suma_decorada = fn_decorador(suma)
tres = suma_decorada(1, 2)
print(tres)

fn_decorador = medir_tiempo_ejecucion(num_decimales=5)
suma_decorada = fn_decorador(suma)
tres = suma_decorada(1, 2)
print(tres)



class PermisoPermitido:
    def __init__(self, permiso):
        self.permiso = permiso

    def __call__(self, fn_a_decorar):
        def wrapper(usuario, *args, **kwargs):
            # Comprobar si el usuario tiene permiso de escritura
            if self.permiso not in usuario["permisos"]:
                print(f"{usuario["nombre"]} no tiene permisos para ejecutar esta función")
                return None

            resultado = fn_a_decorar(usuario, *args, **kwargs)
            return resultado

        return wrapper


@PermisoPermitido("escritura")
def editar_informe(usuario, informe_id):
    print(f"Se ha modificado el informe con id {informe_id}")


usuario1 = {"nombre": "Charly", "permisos": ["escritura", "lectura"]}
usuario2 = {"nombre": "Paco", "permisos": ["lectura"]}
editar_informe(usuario1, 1)
editar_informe(usuario2, 2)