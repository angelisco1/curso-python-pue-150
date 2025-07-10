from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, HTTPException, Unauthorized
import jwt

from api.controllers import auth_bp, ingredients_bp
from api.errors import errors_bp
from api.database import init_db

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(ingredients_bp)
app.register_blueprint(errors_bp)


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=3006)

