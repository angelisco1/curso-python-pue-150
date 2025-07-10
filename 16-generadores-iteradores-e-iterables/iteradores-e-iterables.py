numeros = [1, 2, 3]
print(numeros)

iterador_nums = iter(numeros)
print(iterador_nums)

n = next(iterador_nums)
print(n)

n = next(iterador_nums)
print(n)

n = next(iterador_nums)
print(n)

# iterador_nums = iter(numeros)
# n = next(iterador_nums)
# print(n)

print("----")

# Es un iterador
class Contador:
    def __init__(self, inicial=0, num_maximo=3):
        self.cuenta = inicial
        self.num_maximo = num_maximo

    def __iter__(self):
        return self

    def __next__(self):
        if self.cuenta >= self.num_maximo:
            raise StopIteration

        numero = self.cuenta
        self.cuenta += 1
        return numero


contador = Contador()
num = next(contador)
print(num)

num = next(contador)
print(num)

print("Empieza el bucle for")
for cuenta in contador:
    print(cuenta)

contador = Contador()

print("Empieza el segundo bucle for")
for cuenta in contador:
    print(cuenta)


class IngredientesReceta:
    def __init__(self, lista_ingredientes):
        self.lista_ingredientes = lista_ingredientes

    def __iter__(self):
        return IteradorIngredientes(self.lista_ingredientes)


class IteradorIngredientes:
    def __init__(self, lista_ingredientes):
        self.lista_ingredientes = lista_ingredientes
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.lista_ingredientes):
            raise StopIteration

        ingrediente = self.lista_ingredientes[self.indice]
        self.indice += 1
        return ingrediente


ingredientes_tortilla_patatas = IngredientesReceta(["aceite", "sal", "patatas", "cebolla", "huevo"])

for ing in ingredientes_tortilla_patatas.lista_ingredientes:
    print(ing)

for ing in ingredientes_tortilla_patatas.lista_ingredientes:
    print(ing)

for ing in ingredientes_tortilla_patatas.lista_ingredientes:
    print(ing)


print("-> Usando el iterador")
iterador_ing = iter(ingredientes_tortilla_patatas)
print(next(iterador_ing))
print(next(iterador_ing))
print(next(iterador_ing))

print("-> Usando el iterador en bucles")
for ing in ingredientes_tortilla_patatas:
    print(ing)

for ing in ingredientes_tortilla_patatas:
    print(ing)