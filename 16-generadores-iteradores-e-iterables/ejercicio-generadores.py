# EJERCICIO 1: Implementar un generador que nos vaya generando los números de la secuencia de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# serie de fib -> valor previo + valor actual
# serie(3) -> 0, 1, 1
# serie(7) -> 0, 1, 1, 2, 3, 5, 8
#
# for i in range(10):
#     print(...)

def fibonacci():
    prev, current = 0, 1
    while True:
        yield prev
        prev, current = current, prev + current


generador_fib = fibonacci()
for _ in range(3):
    print(next(generador_fib))


generador_fib = fibonacci()
for _ in range(7):
    print(next(generador_fib))