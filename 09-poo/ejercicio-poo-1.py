# Ejercicio 1
# Crear una clase Serie (título, capítulos, finalizada, capítulos_vistos)
# Añadirle las funcionalidades siguientes:
# - Ver capítulo (modificar capítulos vistos)
# - Obtener los capítulos restantes
# - Obtener si ya la hemos visto

class Serie:

    def __init__(self, titulo, capitulos, capitulos_vistos, finalizada):
        self.titulo = titulo
        self.capitulos = capitulos
        self.capitulos_vistos = capitulos_vistos
        self.finalizada = finalizada

    def ver_capitulo(self):
        if self.capitulos_por_ver() == 0:
            return "Ya has visto todos los capítulos, no puedes ver más."
        self.capitulos_vistos += 1
        return "Has visto otro capítulo"

    def esta_vista(self):
        return self.capitulos_por_ver() == 0 and self.finalizada

    def capitulos_por_ver(self):
        return self.capitulos - self.capitulos_vistos


vikings = Serie("Vikings", 100, 97, True)
game_of_thrones = Serie("Game of Thrones", 100, 100, True)

print(vikings.capitulos_por_ver())
print(vikings.ver_capitulo())
print(vikings.capitulos_por_ver())
print(vikings.esta_vista())

print(game_of_thrones.capitulos_por_ver())
print(game_of_thrones.esta_vista())
print(game_of_thrones.ver_capitulo())


