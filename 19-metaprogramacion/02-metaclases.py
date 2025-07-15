class MiMetaclase(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creando la clase {name} con los atributos {attrs}")

        def incrementar(self):
            self.cuenta += 1
        attrs["incrementar"] = incrementar

        return super().__new__(cls, name, bases, attrs)


class A(metaclass=MiMetaclase):
    cuenta = 0



a = A()
print(a.cuenta)
a.incrementar()
a.incrementar()
a.incrementar()
print(a.cuenta)
