from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, HTTPException, Unauthorized
import jwt

from api.controllers import auth_bp, ingredients_bp, SECRETO
from api.errors import errors_bp
from api.database import init_db

app = Flask(__name__)

@app.before_request
def validate_token():
    unprotected_routes = [
        {"path": "/login", "method": "POST"},
        {"path": "/ingredients", "method": "GET"}
    ]

    not_need_validation = next((route for route in unprotected_routes if route["path"] in request.path and
                                route["method"] == request.method), None)

    if not_need_validation:
        return

    if "authorization" not in request.headers:
        raise Unauthorized("No has enviado el token de autenticación")

    bearer, token = request.headers["authorization"].split(" ")

    try:
        jwt.decode(token, SECRETO, algorithms=["HS256"])
        # except jwt.InvalidSignatureError:
        #     raise Unauthorized("El token es inválido")
        # except jwt.InvalidTokenError:
        #     raise Unauthorized("El token es inválido")
    except (jwt.InvalidSignatureError, jwt.InvalidTokenError):
        raise Unauthorized("El token es inválido")
    except jwt.ExpiredSignatureError:
        raise Unauthorized("El token ha expirado")


app.register_blueprint(auth_bp)
app.register_blueprint(ingredients_bp)
app.register_blueprint(errors_bp)


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=3006)

