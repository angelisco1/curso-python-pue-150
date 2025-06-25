class Animal:
    def __init__(self, nombre, tipo, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} dice '{self.sonido}'")

    def __str__(self):
        print("Animal")
        return f"Animal(nombre={self.nombre}, tipo={self.tipo}, sonido={self.sonido})"

class AnimalVolador(Animal):
    def volar(self):
        print("Puede volar")

    def __str__(self):
        print("AnimalVolador")
        # str_animal = Animal.__str__(self)
        str_animal = super().__str__()
        return f"{str_animal} (es AnimalVolador)"

class AnimalNadador(Animal):
    def nadar(self):
        print("Puede nadar")

    def __str__(self):
        print("AnimalNadador")
        # str_animal = Animal.__str__(self)
        str_animal = super().__str__()
        return f"{str_animal} (es AnimalNadador)"

class Pato(AnimalVolador, AnimalNadador):
    def __init__(self, nombre):
        super().__init__(nombre, "pato", "Cuac cuac")

    def __str__(self):
        print("Pato")
        # str_volador = AnimalVolador.__str__(self)
        # str_nadador = AnimalNadador.__str__(self)
        str_animal = super().__str__()
        return f"{str_animal} (es un Pato)"


willix = Pato("Willix")
willix.volar()
willix.nadar()
willix.hacer_sonido()

print(willix)

print(Pato.__mro__)

# Pinguino
