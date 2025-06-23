
class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni # -> _Persona__dni
        self.dni_oculto = ("*" * 6) + dni[6:]

    def get_dni(self):
        print("Getter del DNI", self)
        return self.__dni

    def set_dni(self, nuevo_dni):
        print("Setter del DNI")
        self.__dni = nuevo_dni

    dni = property(get_dni, set_dni)

    def __setattr__(self, key, value):
        if key == "dni":
            self.dni_oculto = ("*" * 6) + value[6:]
        #   TODO:

    def __getattribute__(self, item):
        if item == "no_existe":
            return "No existe esta propiedad"
        elif item == "dni":
            dni = object.__getattribute__(self, item)
            # self.dni_oculto = ("*" * 6) + dni[6:]
            return dni
        else:
            return object.__getattribute__(self, item)

charly = Persona("Charly", "Falco", "00000000T")
print(charly.dni)
charly.dni += "A" # -> charly.dni = charly.dni + "A"
print(charly.get_dni())
print(charly.dni_oculto)