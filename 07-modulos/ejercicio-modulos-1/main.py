# Ejercicio 1
# Crear un traductor de textos
# Como primer parámetro tiene que recibir una clave que representa el texto a traducir
# Como segundo parámetro tiene que recibir el lenguaje al cual queremos traducir el texto
# El lenguaje de traducción por defecto será el inglés ("en")
# Las traducciones las vamos a tener en un diccionario, es decir, hola -> hello,  hola -> ciao ...
from traductor import traduce

# -- Ejemplo de uso
print(traduce("hola", lang="en")) # hello
print(traduce("hola", lang="it")) # ciao
print(traduce("Abrir", lang="es")) # ciao
print(traduce("no existe", lang="es")) # ciao
print(traduce("patatas")) # potatoes

