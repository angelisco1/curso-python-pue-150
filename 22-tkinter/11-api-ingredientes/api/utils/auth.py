import os
from functools import wraps

from flask import request, current_app
from werkzeug.exceptions import Unauthorized
import jwt
# from ..constants import SECRETO

def validate_token(fn_a_decorar):
    @wraps(fn_a_decorar)
    def wrapper(*args, **kwargs):

        if "authorization" not in request.headers:
            raise Unauthorized("No has enviado el token de autenticación")

        bearer, token = request.headers["authorization"].split(" ")

        try:
            jwt.decode(token, os.getenv("SECRETO"), algorithms=["HS256"])
        except (jwt.InvalidSignatureError, jwt.InvalidTokenError):
            raise Unauthorized("El token es inválido")
        except jwt.ExpiredSignatureError:
            raise Unauthorized("El token ha expirado")

        return fn_a_decorar(*args, **kwargs)

    return wrapper






