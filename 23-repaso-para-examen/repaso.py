from abc import ABC, abstractmethod

# Excepciones
class PizzaError(Exception):
    def __init__(self, message):
        self.message = message


class NotValidPriceError(PizzaError):
    def __init__(self, price):
        super().__init__(f"La pizza no puede tener un precio menor o igual a 0 (actualmente tiene {price})")
        self.price = price


class EmptyIngredientsError(PizzaError):
    def __init__(self, ingredientes):
        super().__init__(f"La pizza no puede tener menos de 3 ingredientes (actualmente tiene {len(ingredientes)})")
        self.ingredientes = ingredientes

class PizzaCookingError(PizzaError):
    def __init__(self):
        super().__init__(f"La pizza ya se está cocinando, no se puede modificar")


# POO
class MetodoCoccion(ABC):
    def __init__(self):
        self.cocinando = False

    @abstractmethod
    def cocinar(self):
        pass

    def sacar_del_horno(self):
        self.cocinando = False

class HornoLenya(MetodoCoccion):
    def cocinar(self):
        self.cocinando = True
        print("Cocinando en el horno de leña. Tardará 15 min")

class HornoElectrico(MetodoCoccion):
    def cocinar(self):
        self.cocinando = True
        print("Cocinando en el horno de leña. Tardará 20 min")



class Pizza:
    porciones = 1

    def __init__(self, nombre, descripcion, precio, ingredientes, metodo_coccion=HornoElectrico()):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.__ingredientes = ingredientes # Name mangling -> _Pizza__ingredientes
        self.metodo_coccion = metodo_coccion

    def cocinar(self):
        self.metodo_coccion.cocinar()

    def sacar_del_horno(self):
        self.metodo_coccion.sacar_del_horno()

    def cortar_en_porciones(self, num_porciones):
        self.porciones = num_porciones

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, nuevos_ingredientes):
        if self.metodo_coccion.cocinando:
            raise PizzaCookingError()
        self.__ingredientes = nuevos_ingredientes


    @classmethod
    def create_1(cls, nombre, descripcion, precio, ingredientes):
        if precio > 0:
            raise ValueError("La pizza tiene que tener un precio mayor a 0")

        if len(ingredientes) > 2:
            raise ValueError("La pizza tiene que tener más de 2 ingredientes para poder hacerla")

        return cls(nombre, descripcion, precio, ingredientes)

    @staticmethod
    def create_2(nombre, descripcion, precio, ingredientes):
        if precio <= 0:
            # raise ValueError("La pizza tiene que tener un precio mayor a 0")
            raise NotValidPriceError(precio)

        if (num_ingredientes := len(ingredientes)) < 3:
            # raise ValueError("La pizza tiene que tener más de 2 ingredientes para poder hacerla")
            raise EmptyIngredientsError(ingredientes)

        return Pizza(nombre, descripcion, precio, ingredientes)

    def __str__(self):
        return f"Pizza(nombre={self.nombre}, descripcion={self.descripcion}...)"

    def __repr__(self):
        return f"Pizza(nombre={self.nombre}, descripcion={self.descripcion}...)"

    def __eq__(self, pizza2):
        return self.ingredientes == pizza2.ingredientes

    def __call__(self):
        print("Se ejecuta cuando llamamos a la instancia como si fuese un método")



bbq = Pizza(
    "BBQ",
    "Pizza de jamon york con bacon y salsa bbq.",
    9.99,
    ["salsa bbq", "jamon york", "bacon", "queso"],
    metodo_coccion=HornoLenya()
)

print(bbq.porciones)
bbq.cortar_en_porciones(8)
print(bbq.porciones)

print(Pizza.porciones)

bbq2 = Pizza(
    "BBQ",
    "Pizza de jamon york con bacon y salsa bbq.",
    9.99,
    ["salsa bbq", "jamon york", "bacon", "queso"],
    metodo_coccion=HornoElectrico()
)

Pizza.cortar_en_porciones(bbq2, 6)

pizzaiola = Pizza.create_2(
    "Pizzaiola",
    "Pizza con jamon de york, ajo, aceite y queso",
    7.5,
    ["jamon york", "ajo", "aceite", "queso"]
)
pizzaiola.cortar_en_porciones(8)
print(pizzaiola)


try:
    pizzaiola2 = Pizza.create_2(
        "Pizzaiola",
        "Pizza con jamon de york, ajo, aceite y queso",
        0,
        ["jamon york", "ajo", "aceite", "queso"]
    )
except NotValidPriceError as e:
    print(e.message)
    print(e.price)


try:
    pizzaiola2 = Pizza.create_2(
        "Pizzaiola",
        "Pizza con jamon de york, ajo, aceite y queso",
        7.5,
        ["aceite"]
    )
except EmptyIngredientsError as e:
    print(e.message)
    print(e.ingredientes)


try:
    pizzaiola.cocinar()
    pizzaiola.ingredientes = ["jamon york", "aceite", "ajo", "queso", "aceitunas"]
except PizzaCookingError as e:
    print(e.message)


print(bbq == bbq2)
bbq2.ingredientes = [*bbq2.ingredientes, "huevo"]
print(bbq == bbq2)

bbq()

class Pedido(ABC):
    @abstractmethod
    def pagar(self):
        pass

class PedidoTienda(Pedido):
    def pagar(self):
        print("Pedido pagado en efectivo")

class PedidoOnline(Pedido):
    def pagar(self):
        print("Pedido pagado con tarjeta")

# Programación funcional y funciones lambda
nums = [1, 2, 3, 4]
doble_nums = [num * 2 for num in nums]
print(doble_nums)

cuadrado_nums = list(map(lambda n: n ** 2, doble_nums))
print(cuadrado_nums)

cuadrado_nums = list(map(lambda n: n ** 2, nums))

cuadrado = lambda n: n ** 2
cuadrado_nums = []
for n in nums:
    cuadrado_nums.append(cuadrado(n))
print(cuadrado_nums)

nums_mayores_de_2 = list(filter(lambda n: n > 2, nums))
print(nums_mayores_de_2)


# Closures
def calculadora_iva(iva):
    a = 1
    def calcular(cantidad):
        print(a)
        return cantidad * iva
    return calcular


calculadora_21_iva = calculadora_iva(0.21)
calculadora_10_iva = calculadora_iva(0.10)

print(calculadora_21_iva(20))
print(calculadora_21_iva(34))

print(calculadora_10_iva(34))

print(calculadora_10_iva.__closure__[0].cell_contents)
print(calculadora_10_iva.__closure__[1].cell_contents)


# Iteradores y generadores
class Iterador:
    def __init__(self):
        self.cuenta = 0

    def __iter__(self):
        return self

    def __next__(self):
        cuenta_actual = self.cuenta
        self.cuenta += 1
        return cuenta_actual

it = Iterador()
print(next(it))
print(next(it))
print(next(it))

for i in it:
    if i == 9:
        break
    print(i)


def contador(n):
    i = 0
    while i < n:
        yield i
        i += 1


generador = contador(3)
print(next(generador))
print(next(generador))

generador2 = (n * 2 for n in range(4))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
# print(next(generador2))

