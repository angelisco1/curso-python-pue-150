class Persona:
    pass

print(type(Persona))

def contar(self):
    self.cuenta += 1

# type(__name__, __bases__, __dict__)
Contador = type("Contador", (), {
    "cuenta": 0,
    "contar": contar
})

MiInt = type("MiInt", (int,), {})

contador = Contador()

print(contador.cuenta)
contador.contar()
contador.contar()
contador.contar()
print(contador.cuenta)

class Contador2:
    # atributo de clase
    cuenta = 0

    def contar(self):
        self.cuenta += 1

contador2 = Contador2()

print(contador2.cuenta)
contador2.contar()
contador2.contar()
contador2.contar()
print(contador2.cuenta)

# ORM
# Validar campos
# Serialización
# ...

print(Contador.__name__)
print(Contador.__bases__)
print(Contador.__dict__)

int(3)

def init(self, cuenta_inicial):
    # Ahora lo estamos añadiendo como atributo de la instancia
    self.cuenta = cuenta_inicial

Contador3 = type("Contador3", (), {
    "__init__": init,
    "contar": contar
})

contador3 = Contador3(5)
contador3.contar()
print(contador3.cuenta)

print(Contador3.__dict__)
print(contador3.__dict__)



class ComandosBot:

    def buscar(self, tema):
        print(f"Buscar información sobre {tema}")



class GestorComandos:
    def __init__(self, gestor):
        self.gestor = gestor

    def agregar_comando(self, nombre_comando, fn_comando):
        if hasattr(self.gestor, nombre_comando):
            return f"El comando {nombre_comando} ya existe"

        setattr(self.gestor, nombre_comando, fn_comando)
        return f"Se ha añadido el comando {nombre_comando}"

    def ejecutar_comando(self, comando, *args):
        if hasattr(self.gestor, comando):
            fn_comando = getattr(self.gestor, comando)
            if callable(fn_comando):
                try:
                    return fn_comando(*args)
                except Exception:
                    return f"Hay un error al ejecutar el comando {comando}"
            return f"El comando {comando} no es una función"
        return f"El comando {comando} no existe"




comandos_bot = ComandosBot()
gestor_del_bot = GestorComandos(comandos_bot)
print(ComandosBot.__dict__)

# lambda params: operacion
# def suma(n1, n2):
#     print("algo")

gestor_del_bot.agregar_comando("sumar", lambda n1, n2: n1 + n2)
tres = gestor_del_bot.ejecutar_comando("sumar", 1, 2)
print(tres)


