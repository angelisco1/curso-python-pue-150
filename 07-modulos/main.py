import math
# from operaciones import resta
# from math import *
# import operaciones
from operaciones import resta as mi_resta
# from math import pi as MI_PI
import operaciones as op
import random

# print(math.pi)

def resta(n1, n2):
    if n1 < 0 or n2 < 0:
        return "Error"
    return n1 - n2

# print(operaciones.MI_PI)
# print(operaciones.suma(1, 2))
# print(MI_PI)
# print(mi_resta(-1, 2))
# print(resta(-1, 2))

print(op.suma(1, 2))

# print(suma(1, 2))

# Nos devuelve donde está definido la función/variable...
print(resta.__module__)
print(mi_resta.__module__)

print(math.sqrt(4))
print(math.pow(2, 4))

print(random.randint(1, 50))
print(random.random())

recetas = ["salmorejo", "tortilla de patatas", "pollo asado"]
print(random.choice(recetas))

baraja = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(random.sample(baraja, 3))

random.shuffle(baraja)
print(baraja)
