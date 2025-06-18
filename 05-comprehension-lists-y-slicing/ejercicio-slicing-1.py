# Ejercicio 1
# Crear una función, que nos diga si un texto es palíndromo o no lo es
# Un texto palíndromo es aquel que se lee igual de izq a der que de der a izq
# Ej: La ruta natural

replace_letras = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
}
# replace_letras = [('á', 'a'), ('é', 'e')]

texto = "La ruta natural."

def es_palindromo(texto):
    texto_minus = texto.lower()
    texto_sin_espacios = texto_minus.replace(" ", "").replace(".", "")
    for old, new in replace_letras.items():
        texto_sin_espacios = texto_sin_espacios.replace(old, new)
    # if texto_sin_espacios == texto_sin_espacios[::-1]:
    #     return True
    # return False
    return texto_sin_espacios == texto_sin_espacios[::-1]

print(es_palindromo(texto))
print(es_palindromo("Eva usaba rimel y le miraba suave"))
print(es_palindromo("Hola mundo"))

print(es_palindromo("Dábale arroz a la zorra el Abad"))