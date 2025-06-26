lista = [1, 0, 3, "a"]
# print(lista[10])

# elem = lista.pop("a")

# # print(1000/int(numero))
#
# numero = input("Vas a dividir el número 300 entre: ")
#
# while True:
#     try:
#         print(300/int(numero))
#         break
#     except Exception:
#         print(f"El número {numero} no se puede utilizar")
#         numero = input("Vuelve a introducir un número: ")


numero = input("Vas a dividir el número de la lista que está en la posición: ")

while True:
    try:
        print(300/lista[int(numero)])
        break
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
        numero = input("Vuelve a introducir una posición de la lista que tenga un número distinto a 0: ")
    except TypeError:
        print("El tipo de dato no se puede usar para hacer esta división")
        numero = input("Vuelve a introducir una posición de la lista que tenga un tipo de dato válido: ")
    except IndexError:
        print(f"La lista no tiene un índice como el que has introducido, pon uno entre el 0 y {len(lista) - 1}")
        numero = input("Vuelve a introducir una posición dentro del rango válido: ")
    finally:
        print("Siempre se va a ejecutar esto")


def verificar_numero_positivo(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo")
    return True

# try:
#     verificar_numero_positivo(-1)
# except ValueError:
#     TODO: ver el objeto error
#     # Escribe el error en el archivo log
#     pass

print("FIN")