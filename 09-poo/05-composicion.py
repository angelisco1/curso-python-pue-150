from datetime import datetime, timedelta


class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()


motor = Motor()
seat = Coche(motor)
seat.arrancar()
