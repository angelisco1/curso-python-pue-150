import os

from flask import Blueprint, request, jsonify, current_app
from werkzeug.exceptions import Unauthorized
import jwt
# from ..constants import SECRETO
from ..utils import log


usuarios_registrados = [
    { "id": 1, "name": "Charly", "email": "cfalco@gmail.com", "password": "1234", "role": "ADMIN" },
    { "id": 2, "name": "Octavia", "email": "oblake@gmail.com", "password": "1234", "role": "FREE" },
]

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
@log
def login():
    credenciales = request.json

    usuario = next((usuario for usuario in usuarios_registrados if usuario["email"] == credenciales["email"] and
                    usuario["password"] == credenciales["password"]), None)

    if not usuario:
        raise Unauthorized(f"Las credenciales son inválidas")

    token = jwt.encode({
        "name": usuario["name"],
        "role": usuario["role"],
    }, os.getenv("SECRETO"))

    # token = jwt.encode({
    #     "name": usuario["name"],
    #     "role": usuario["role"],
    # }, SECRETO)

    return jsonify({ "token": token }), 201
