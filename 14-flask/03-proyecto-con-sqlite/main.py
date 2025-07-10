from flask import Flask
from api.controllers import ingredients_bp
from api.database import init_db

app = Flask(__name__)

app.register_blueprint(ingredients_bp)


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=3006)

