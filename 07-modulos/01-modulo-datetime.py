from datetime import datetime, date, time, timedelta
from time import strftime

ahora = datetime.now()
print(ahora)

fecha_actual = date.today()
print(fecha_actual)

una_fecha = datetime(2014, 8, 12, 13, 46, 23)
print(una_fecha)

mi_cumple = date(1999, 6, 25)
print(mi_cumple)

la_hora_pi = time(3, 14, 15)
print(la_hora_pi)


print(una_fecha.year)
print(una_fecha.minute)
print(mi_cumple.day)
print(la_hora_pi.second)


# ahora.hour = 21
ahora_a_las_9_de_la_noche = ahora.replace(hour=21)
print(ahora_a_las_9_de_la_noche)

# Permite crear una nueva fecha a partir de otra, haciendole ciertos cambios
ahora_a_las_9_de_la_noche = ahora.replace(hour=21, minute=0, second=0, microsecond=0)
print(ahora_a_las_9_de_la_noche)

# Representan las fechas minima y maxima que se pueden obtener con el datetime
print(datetime.min)
print(datetime.max)


# usuario = {
#     "nombre": "Ángel",
#     "email": "angel@gmail.com"
# }
#
# credenciales = {
#     "email": "esteeselsegundo@email.com",
#     "password": "1234"
# }
#
# usuario.update(credenciales)
# print(usuario)

hoy_a_primera_hora = datetime.combine(ahora, datetime.min.time())
print(hoy_a_primera_hora)
ahora_a_las_9_de_la_noche = datetime.combine(ahora, datetime.min.time()).replace(hour=21)
print(ahora_a_las_9_de_la_noche)


# Formateo de fechas

ahora = datetime.now()
# %Y -> año
# %m -> mes
# %d -> día
# %H -> hora
# %M -> minutos
# %s -> segundos

fecha_actual_formateada = ahora.strftime("%d/%m/%Y %H:%M")
print(fecha_actual_formateada)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
print(ahora.strftime(f"%d de {meses[int(ahora.month) - 1]} de %Y"))

fecha = datetime.strptime("2025_06_24", "%Y_%m_%d")
print(fecha)
print(fecha.date())
print(fecha.day)


# Timedelta -> representa una duración
una_duracion = timedelta(days=2, hours=20)
dos_years = timedelta(days=365 * 2)
print(dos_years)

print(ahora + dos_years)
print(ahora - timedelta(days=3))


duracion_concierto_los_del_rio = datetime(2024, 9, 10, 20) - datetime(2024, 9, 10, 18)
print(duracion_concierto_los_del_rio)

duracion_festival_medusa = datetime(2024, 7, 12, 23) - datetime(2024, 7, 10, 18)
print(duracion_festival_medusa)


# Timestamp
print(ahora.timestamp())

una_fecha_timestamp = una_fecha.timestamp()

# Obtener una fecha a partir de un timestamp
una_fecha = datetime.fromtimestamp(una_fecha_timestamp)
print(una_fecha)











