# EJERCICIO: Crear un decorador para loggear en un archivo "main.log" las llamadas que llegan a la aplicación:
# - Recibida petición a login con los datos (introducir los args, kwargs, request.json...)
# - Recibida petición a get_ingredients con los datos (introducir los args, kwargs, request.json...)
import logging
from functools import wraps
from flask import request

logger = logging.getLogger("api.utils.logs")

formato1 = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s>%(funcName)s>Nº%(lineno)d - %(message)s",
    datefmt="%Y/%m/%d_%H:%M:%S"
)

handler = logging.FileHandler(filename="main.log")
handler.setFormatter(formato1)

logger.addHandler(handler)

handler2 = logging.StreamHandler()
handler2.setFormatter(formato1)

logger.addHandler(handler2)
logger.setLevel(logging.INFO)


def serialize(clase):
    def decorador(fn_a_decorar):
        @wraps(fn_a_decorar)
        def wrapper(*args, **kwargs):

            body = request.get_json(silent=True)
            request.body = clase.from_dict(body)

            return fn_a_decorar(*args, **kwargs)

        return wrapper
    return decorador













