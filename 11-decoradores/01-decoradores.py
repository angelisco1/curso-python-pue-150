import time

# Decorador
def log(fn_decorada):
    def wrapper(*args, **kwargs):
        print(f"Se va a ejecutar la función {fn_decorada.__name__} con los argumentos {args}")
        resultado = fn_decorada(*args, **kwargs)
        print(f"El resultado de la ejecución es: {resultado}")
        return resultado

    return wrapper


# Decorando la función suma con el decorador log
@log
def resta(n1, n2):
    return n1 - n2

# Esta sería la función wrapper (que es la resta decorada)
resta(1, 2)


def suma(n1, n2):
    return n1 + n2

suma_decorada = log(suma)
tres = suma_decorada(1, 2)
print(tres)



def medir_tiempo_ejecucion(fn_decorada):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        print(f"Inicio: {inicio}")

        resultado = fn_decorada(*args, **kwargs)

        fin = time.time()
        print(f"Fin: {fin}")

        print(f"La ejecución de la función {fn_decorada.__name__} ha sido de {fin - inicio} segundos")
        return resultado
    return wrapper

@medir_tiempo_ejecucion
def suma(n1, n2):
    # time.sleep(2)
    return n1 + n2


suma(1000, 30000000)
suma(1, 3)


class MiDecoradorLog:
    def __init__(self, fn_decorada):
        self.fn = fn_decorada

    # Esto se ejecuta cuando llamamos a la instancia de la clase como si esta fuese una función, cuando no lo es
    def __call__(self, *args, **kwargs):
        print("Estás ejecutando la instancia como si esta fuese una fn")
        print(f"Se va a ejecutar la función {self.fn.__name__} con los argumentos {args}")
        resultado = self.fn(*args, **kwargs)
        print(f"El resultado de la ejecución es: {resultado}")
        return resultado


def suma(n1, n2):
    return n1 + n2

instancia_del_decorador = MiDecoradorLog(suma)
# print(instancia_del_decorador.fn(10, 2))
print(instancia_del_decorador(2, 3))


@MiDecoradorLog
def suma(n1, n2):
    return n1 + n2

cinco = suma(2, 3)
print(cinco)