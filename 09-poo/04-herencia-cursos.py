from datetime import datetime, timedelta

class Curso:
    def __init__(self, curso_id, nombre, num_plazas):
        self.curso_id = curso_id
        self.nombre = nombre
        self.num_plazas = num_plazas
        self.lista_alumnos = []

    def inscribir_alumnos(self, alumno):
        if self.num_plazas > len(self.lista_alumnos) and alumno not in self.lista_alumnos:
            self.lista_alumnos.append(alumno)
            print(f"El alumno {alumno} se ha inscrito en el curso {self.nombre}")
        else:
            print(f"El alumno {alumno} no se ha podido inscribir en el curso {self.nombre}")


class CursoPresencial(Curso):
    def __init__(self, curso_id, nombre, num_plazas, direccion):
        super().__init__(curso_id, nombre, num_plazas)
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

curso_python.inscribir_alumnos(angel)
curso_python.inscribir_alumnos(sara)
curso_python.inscribir_alumnos(paco)

curso_python.registrar_asistencia(angel, "2025-06-24")
curso_python.registrar_asistencia(angel, "2025-06-25")
curso_python.registrar_asistencia(sara, "2025-06-25")

print(f"{angel} ha asistido al {curso_python.porcentaje_asistencia(angel)}% del curso")
print(f"{sara} ha asistido al {curso_python.porcentaje_asistencia(sara)}% del curso")



class CursoOnline(Curso):
    def __init__(self, curso_id, nombre, num_plazas, plataforma):
        super().__init__(curso_id, nombre, num_plazas)
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

curso_python.inscribir_alumnos(angel)
curso_python.inscribir_alumnos(sara)

curso_python.registrar_asistencia(angel, "2025-06-24")
curso_python.registrar_asistencia(angel, "2025-06-25")
curso_python.registrar_asistencia(sara, "2025-06-25")

curso_python.get_reporte_asistencia()


class CursoEnlatado(Curso):
    def __init__(self, curso_id, nombre, num_plazas, plataforma, fecha_grabacion, duracion):
        super().__init__(curso_id, nombre, num_plazas)
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


curso_python = CursoEnlatado("Enlatado1", "Python", None, "Coursera", "12/10/2021", 500)
# curso_python = CursoEnlatado("Enlatado1", "Python", 100, "Coursera", "12/10/2021", 500)

angel = "Ángel"
sara = "Sara"
curso_python.inscribir_alumnos(angel)
curso_python.inscribir_alumnos(sara)

print(curso_python.esta_obsoleto())
