# Ejercicio 1
# Crear una lista que tenga la cuenta del número de elementos que tiene
# No hay que hacer len(mi_lista) para obtenerlos

class ListaConLength(list):
    def __init__(self, *args):
        super().__init__(args)
        num_elements = 0
        for _ in args:
            num_elements += 1
        self.length = num_elements
        
    def append(self, element):
        super().append(element)
        self.length += 1

    def pop(self, indice=-1):
        element_to_delete = super().pop(indice)
        self.length -= 1
        return element_to_delete


lista = ListaConLength(1, 2, 3, 4, 5)
print(lista.length)
lista.append(6)
lista.append(7)
print(lista.length)
lista.pop(1)
lista.pop()
print(lista.length)

# print(mi_lista.length)
# print(mi_lista.get_length())


class ListaConLength2(list):
    def __init__(self, lista):
        super().__init__(lista)
        # print(self)

    def get_length(self):
        num_elements = 0
        for _ in self:
            num_elements += 1
        return num_elements

lista = ListaConLength2([1, 2, 3, 4, 5])
print(lista.get_length())
lista.append(6)
lista.append(7)
print(lista.get_length())
lista.pop(1)
lista.pop()
print(lista.get_length())