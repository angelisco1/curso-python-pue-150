# Ejemplo del DNI que hereda de str y sobreescribe la función de suma
import re

class DNI(str):
    def __init__(self, dni):
        self.dni = dni

    def __add__(self, valor_a_sumar):
        if not re.search("[A-Za-z]{1}$", self.dni):
            return self.dni + valor_a_sumar
        return self.dni


dni1 = DNI("00000000T")
dni2 = DNI("00000000")

print(dni1 + "R")
print(dni2 + "R")

