def suma(n1, n2):
    return n1 + n2

numero1 = 10
numero2 = -3
res = suma(numero1, numero2)
print(res)

def resta(n1, n2):
    return n1 - n2

res = resta(1, 2)
print(res)


def saludar(nombre="mundo"):
    """Función que saluda a una persona"""
    print(f"Hola {nombre}")

saludar("Charly")
saludar("Ángel")
sara = "Sara"
saludar(sara)
saludar()
saludar(nombre=sara)

# peticion a la API
# usuario
# saludar(usuario)


def add_element(item, lista=[]):
    lista.append(item)
    return lista

l1 = [1, 2]
# l1 = add_element(3, l1)
add_element(3, l1)
print(l1)

l2 = add_element(2)
print(l2)

l3 = add_element(3)
print(l3)

def add_element(item, lista=None):
    if not lista:
        lista = []
    lista.append(item)
    return lista


l2 = add_element(2)
print(l2)

l3 = add_element(3)
print(l3)



def get_ticket_loteria(sorteo, *nums):
    lista_nums = []
    for n in nums:
        lista_nums.append(str(n))
    return f"""Boleto para {sorteo}
        {" - ".join(lista_nums)}"""

boleto = get_ticket_loteria("Bonoloto", 1, 17, 26, 28, 39)
print(boleto)

boleto = get_ticket_loteria("Primitiva", 1, 17, 26, 28, 39, 47)
print(boleto)


lista_productos = [
    { "nombre": "USB 16GB", "precio": 8, "stock": 300 },
    { "nombre": "Cargador universal Tipo C", "precio": 11, "stock": 140 },
    { "nombre": "Hub 3 USB, 1 Ethernet, 2 HDMI", "precio": 39, "stock": 70 },
    { "nombre": "Mini ventilador", "precio": 30, "stock": 15 },
]

def filtrar_productos(*args, nombre=None, precio_max=None, stock=None, **kwargs):
    print(args)
    print(kwargs)
    lista_productos_filtrados = []
    if nombre:
        for producto in lista_productos:
            if nombre.lower() in producto["nombre"].lower():
                lista_productos_filtrados.append(producto)
    if precio_max:
        for producto in lista_productos:
            if producto["precio"] <= precio_max:
                lista_productos_filtrados.append(producto)
    if stock:
        for producto in lista_productos:
            if producto["stock"] <= stock:
                lista_productos_filtrados.append(producto)

    return lista_productos_filtrados

print(filtrar_productos(precio_max=18))

productos_filtrados = filtrar_productos(10, 20,  precio_max=18, nombre="usb", precio_min=10)
for producto in productos_filtrados:
    print(f"{producto[f"nombre"]}: {producto["precio"]}€ (Stock: {producto["stock"]})")


def fn(*args, n1=0, **kwargs):
    print(kwargs)

fn(1, 2, 3, n1=1, es_verdad=True, texto="Hola mundo")

# def len(lista):
#     return 0
#
# print(len([1, 2, 3]))


# Ámbito global
a = 1

def fn3():
    a = 7

def fn0():
    a = 0

    def fn1():
        # Ámbito enclosing
        # a = 2

        def fn2():
            # Ámbito local
            global a
            # nonlocal a
            a = 3
            print(f"FN2: {a}")

        fn2()

        print(f"FN1: {a}")

    fn1()

    print(f"FN0: {a}")

fn0()

print(f"Fuera: {a}")



# Funciones recursivas
# 5 * 4 * 3 * 2 * 1
# 5! -> 5 * 4!
# 4! -> 4 * 3!
def factorial(num):
    if num == 1:
        return num
    res_factorial_anterior = factorial(num - 1)
    return num * res_factorial_anterior

# print(factorial(1000))



