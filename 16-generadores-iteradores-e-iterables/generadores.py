def generar_hasta_3():
    yield 1
    yield 2
    yield 3

generador = generar_hasta_3()
print(next(generador))
print(next(generador))

def contar_hasta(n):
    i = 0
    while i < n:
        print(f"Antes del yield, con i = {i}")
        yield i
        print(f"Después del yield, con i = {i}")
        i += 1

generador_hasta_3 = contar_hasta(3)
print(next(generador_hasta_3))
print("--- Vamos a pedir otro valor")
print(next(generador_hasta_3))

for n in generador_hasta_3:
    print(n)

print("--- Después de haberlo iterado una vez")
for n in generador_hasta_3:
    print(n)


# Nos permiten trabajar con secuencias infinitas
def contar_hasta_infinito():
    i = 0
    while True:
        yield i
        # print(i)
        i += 1

print("Contador hasta infinito")
contador_inf = contar_hasta_infinito()
print(next(contador_inf))
print(next(contador_inf))
print(next(contador_inf))
print(next(contador_inf))
print(next(contador_inf))
print(next(contador_inf))
print(next(contador_inf))


dobles = (i * 2 for i in range(5))
print(next(dobles))
print("Empieza el bucle")
for doble in dobles:
    print(doble)




