import random
from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class EstrategiaPagos(ABC):
    @abstractmethod
    def pagar(self, datos_pago):
        pass

class PagoTarjeta(EstrategiaPagos):
    def pagar(self, datos_pago):
        num_tarjeta, fecha_caducidad, cvc = datos_pago.values()
        # Aquí va la lógica de usar alguna API (como redsys) para realizar el pago
        print(f"El alumno ha pagado con una tarjeta ({num_tarjeta} - {fecha_caducidad} - {cvc})")
        return random.choice([True, False, True, True])

class PagoPaypal(EstrategiaPagos):
    def pagar(self, datos_pago):
        email, password = datos_pago.values()
        # Aquí va la lógica de usar la API de Paypal para realizar el pago
        print(f"El alumno ha pagado con su cuenta de Paypal ({email} - {password})")
        return random.choice([True, False, True, True])

class PagoEfectivo(EstrategiaPagos):
    def pagar(self):
        print(f"El alumno ha pagado en efectivo")
        return True


class EstrategiaInscripciones(ABC):

    @abstractmethod
    def puede_inscribirse(self, curso, alumno):
        # raise NotImplementedError
        pass

    def inscribir(self, curso, alumno, estrategia_pagos, datos_pago):
        if self.puede_inscribirse(curso, alumno):
            ha_pagado = estrategia_pagos.pagar(datos_pago)
            if not ha_pagado:
                print(f"El alumno {alumno} no se ha inscrito en el curso {curso.nombre} porque el pago ha fallado")
                return

            curso.lista_alumnos.append(alumno)
            print(f"El alumno {alumno} se ha inscrito en el curso {curso.nombre}")
        else:
            print(f"El alumno {alumno} no se ha podido inscribir en el curso {curso.nombre}")


class InscripcionesLimitadas(EstrategiaInscripciones):
    def __init__(self, num_plazas):
        self.num_plazas = num_plazas

    def puede_inscribirse(self, curso, alumno):
        return self.num_plazas > len(curso.lista_alumnos) and alumno not in curso.lista_alumnos


class InscripcionesIlimitadas(EstrategiaInscripciones):
    def puede_inscribirse(self, curso, alumno):
        return alumno not in curso.lista_alumnos




class Curso:
    def __init__(self, curso_id, nombre, estrategia_inscripciones, estrategias_pagos):
        self.curso_id = curso_id
        self.nombre = nombre
        self.lista_alumnos = []
        self.estrategia_inscripciones = estrategia_inscripciones
        self.estrategias_pagos = estrategias_pagos

    def inscribir_alumnos(self, alumno, datos_pago):
        # if self.num_plazas > len(self.lista_alumnos) and alumno not in self.lista_alumnos:
        #     self.lista_alumnos.append(alumno)
        #     print(f"El alumno {alumno} se ha inscrito en el curso {self.nombre}")
        # else:
        #     print(f"El alumno {alumno} no se ha podido inscribir en el curso {self.nombre}")
        if datos_pago["metodo"] not in self.estrategias_pagos:
            print(f"No puedes usar el pago por {datos_pago["metodo"]} para inscribirte en este curso")
            return
        estrategia_pago = self.estrategias_pagos[datos_pago["metodo"]]
        self.estrategia_inscripciones.inscribir(self, alumno, estrategia_pago, datos_pago["detalles"])


class CursoPresencial(Curso):
    def __init__(self, curso_id, nombre, num_plazas, direccion):
        super().__init__(curso_id, nombre, InscripcionesLimitadas(num_plazas), {
            "tarjeta": PagoTarjeta()
        })
        self.direccion = direccion
        self.sesiones = [] # -> lista de fechas en las que hay clase
        self.asistencias = {} # -> diccionario con los alumnos como claves, y el valor sería una lista de fechas

    def agregar_sesion(self, fecha):
        self.sesiones.append(fecha)

    def registrar_asistencia(self, alumno, fecha):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está apuntado en el curso {self.nombre}")
            return
        if fecha not in self.sesiones:
            print(f"La fecha {fecha} no está en el horario del curso")
            return
        if fecha in self.asistencias.get(alumno, []):
            print(f"La fecha {fecha} ya está registrada para el alumno {alumno}")
            return

        # if alumno not in self.asistencias:
        #     self.asistencias[alumno] = [fecha]
        # else:
        #     self.asistencias[alumno].append(fecha)
        self.asistencias.setdefault(alumno, []).append(fecha)
        print(f"El alumno {alumno} ha asistido a la clase del {fecha}")

    def porcentaje_asistencia(self, alumno):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está en el curso {self.nombre}")
            return None
        total_clases = len(self.sesiones)
        total_asistencias_alumno = len(self.asistencias.get(alumno, []))
        return round((total_asistencias_alumno / total_clases) * 100, 2)


curso_python = CursoPresencial("Presencial1", "Python", 2, "C/ Norte 29, 1C, 28329, Ciudad sin nombre, Madrid")
curso_python.agregar_sesion("2025-06-24")
curso_python.agregar_sesion("2025-06-25")
curso_python.agregar_sesion("2025-06-26")

angel = "Ángel"
sara = "Sara"
paco = "Paco"

curso_python.inscribir_alumnos(angel, { "metodo": "tarjeta", "detalles": { "num_tarjeta": "1234", "cvc": 123,
                                                                           "fecha_caducidad": "2027-12-13" } })
curso_python.inscribir_alumnos(sara, { "metodo": "paypal", "detalles": { "email": "sara@gmail.com", "password": "1234" } })
curso_python.inscribir_alumnos(paco, { "metodo": "paypal", "detalles": { "email": "sara@gmail.com", "password": "1234" } })

curso_python.registrar_asistencia(angel, "2025-06-24")
curso_python.registrar_asistencia(angel, "2025-06-25")
curso_python.registrar_asistencia(sara, "2025-06-25")

print(f"{angel} ha asistido al {curso_python.porcentaje_asistencia(angel)}% del curso")
print(f"{sara} ha asistido al {curso_python.porcentaje_asistencia(sara)}% del curso")



class CursoOnline(Curso):
    def __init__(self, curso_id, nombre, num_plazas, plataforma):
        super().__init__(curso_id, nombre, InscripcionesLimitadas(num_plazas), {
            "tarjeta": PagoTarjeta(),
            "paypal": PagoPaypal(),
        })
        self.plataforma = plataforma
        self.sesiones = []
        self.asistencias = {}

    def agregar_sesion(self, fecha):
        self.sesiones.append(fecha)

    def registrar_asistencia(self, alumno, fecha):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está apuntado en el curso {self.nombre}")
            return
        if fecha not in self.sesiones:
            print(f"La fecha {fecha} no está en el horario del curso")
            return
        if fecha in self.asistencias.get(alumno, []):
            print(f"La fecha {fecha} ya está registrada para el alumno {alumno}")
            return
        self.asistencias.setdefault(alumno, []).append(fecha)
        print(f"El alumno {alumno} ha asistido a la clase del {fecha}")

    def porcentaje_asistencia(self, alumno):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está en el curso {self.nombre}")
            return None
        total_clases = len(self.sesiones)
        total_asistencias_alumno = len(self.asistencias.get(alumno, []))
        return round((total_asistencias_alumno / total_clases) * 100, 2)

    def get_reporte_asistencia(self):
        print(f"Reporte de asistencia del curso {self.nombre}")
        for alumno in self.lista_alumnos:
            porcentaje = self.porcentaje_asistencia(alumno)
            print(f"El alumno {alumno} ha asistido al {porcentaje}% del curso")


curso_python = CursoOnline("Online1", "Python", 2, "Zoom")
curso_python.agregar_sesion("2025-06-24")
curso_python.agregar_sesion("2025-06-25")

angel = "Ángel"
sara = "Sara"

curso_python.inscribir_alumnos(angel, { "metodo": "tarjeta", "detalles": { "num_tarjeta": "1234", "cvc": 123,
                                                                           "fecha_caducidad": "2027-12-13" } })
curso_python.inscribir_alumnos(sara, { "metodo": "paypal", "detalles": { "email": "sara@gmail.com", "password": "1234" } })

curso_python.registrar_asistencia(angel, "2025-06-24")
curso_python.registrar_asistencia(angel, "2025-06-25")
curso_python.registrar_asistencia(sara, "2025-06-25")

curso_python.get_reporte_asistencia()


class CursoEnlatado(Curso):
    def __init__(self, curso_id, nombre, plataforma, fecha_grabacion, duracion):
        super().__init__(curso_id, nombre, InscripcionesIlimitadas(), {
            "paypal": PagoPaypal()
        })
        self.plataforma = plataforma
        self.fecha_grabacion = fecha_grabacion
        self.duracion = duracion
        self.progreso = {}

    def esta_obsoleto(self):
        dos_years = timedelta(days=365 * 2)
        return (datetime.now() - datetime.strptime(self.fecha_grabacion, "%d/%m/%Y")) > dos_years

    def ver_curso(self, alumno, min_visualizados):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está inscrito en el curso {self.nombre}")
            return

        progreso_alumno = self.progreso.setdefault(alumno, 0) + min_visualizados
        self.progreso[alumno] = progreso_alumno


curso_python = CursoEnlatado("Enlatado1", "Python", "Coursera", "12/10/2021", 500)
# curso_python = CursoEnlatado("Enlatado1", "Python", 100, "Coursera", "12/10/2021", 500)

angel = "Ángel"
sara = "Sara"
curso_python.inscribir_alumnos(angel, { "metodo": "tarjeta", "detalles": { "num_tarjeta": "1234", "cvc": 123,
                                                                           "fecha_caducidad": "2027-12-13" } })
curso_python.inscribir_alumnos(sara, { "metodo": "paypal", "detalles": { "email": "sara@gmail.com", "password": "1234" } })

print(curso_python.esta_obsoleto())
