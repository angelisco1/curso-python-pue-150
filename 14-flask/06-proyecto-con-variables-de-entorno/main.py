import os
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, HTTPException, Unauthorized
import jwt
from dotenv import load_dotenv

from api.controllers import auth_bp, ingredients_bp
from api.errors import errors_bp
from api.database import init_db

# Para que cargue las variables de entorno de producción, hay que lanzar el comando:
# $ FLASK_ENV=production python main.py
# Y para el de desarrollo sirve con esto:
# $ python main.py

app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env.development")

app.config["SECRETO"] = os.getenv("SECRETO")
app.config["CSV_PATH"] = os.getenv("CSV_PATH")
app.config["DB_PATH"] = os.getenv("DB_PATH")

app.register_blueprint(auth_bp)
app.register_blueprint(ingredients_bp)
app.register_blueprint(errors_bp)


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=3006)

