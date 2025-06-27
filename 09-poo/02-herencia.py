import random


class Animal:

    def __init__(self, nombre, tipo, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} dice '{self.sonido}'")


# Es un subtipo de algo
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "perro", "guau guau")
        self.num_patas = 4
        # self.num_alas = 0

    # def hacer_sonido(self):
    #     print(f"{self.nombre} dice 'guau guau'!")

    def correr(self):
        print("Estoy corriendo")


class Pajaro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "pajaro", "pio pio")
        self.num_patas = 2
        self.num_alas = 2

    # def hacer_sonido(self):
    #     print(f"{self.nombre} dice 'pio pio'!")

    def volar(self):
        print("Estoy volando")


balto = Perro("Balto")
balto.hacer_sonido()
balto.correr()

piolin = Pajaro("Piolín")
piolin.hacer_sonido()
piolin.volar()


class Empleado:
    def __init__(self, nombre, salario_neto_anual):
        self.nombre = nombre
        self.salario_neto_anual = salario_neto_anual
        self.id = random.randint(0, 50)

    def get_salario_neto_mensual(self):
        return self.salario_neto_anual / 12


class Desarrollador(Empleado):
    def __init__(self, nombre, salario_neto_anual):
        super().__init__(nombre, salario_neto_anual)
        self.bono_mensual = 100

    def get_salario_neto_mensual(self):
        return super().get_salario_neto_mensual() + self.bono_mensual


class Gerente(Empleado):
    def __init__(self, nombre, salario_neto_anual, num_subordinados):
        super().__init__(nombre, salario_neto_anual)
        self.bono_mensual = 50
        self.num_subordinados = num_subordinados

    def get_salario_neto_mensual(self):
        return super().get_salario_neto_mensual() + (self.bono_mensual * self.num_subordinados)


class Ventas(Empleado):
    def __init__(self, nombre, salario_neto_anual):
        super().__init__(nombre, salario_neto_anual)
        self.ventas_realizadas = []
        self.porcentaje_por_venta = 0.05

    def get_salario_neto_mensual(self):
        bono_por_ventas = sum(self.ventas_realizadas) * self.porcentaje_por_venta
        return super().get_salario_neto_mensual() + bono_por_ventas

    def venta(self, total_venta):
        self.ventas_realizadas.append(total_venta)


# Podríamos tener las clases CEO y CTO que como ya cobran mucho, no tienen bono, por tanto su sueldo es el anual / 12
class EmpleadoSinBono(Empleado):
    def __init__(self, nombre, salario_neto_anual):
        super().__init__(nombre, salario_neto_anual)



andrea = Ventas("Andrea", 25000)
andrea.venta(300)
andrea.venta(500)
andrea.venta(200)
print(andrea.get_salario_neto_mensual())

charly = Desarrollador("Charly", 30000)
print(charly.get_salario_neto_mensual())

print(charly.id)
print(andrea.id)

andrea.id = 37
print(charly.id)
print(andrea.id)


