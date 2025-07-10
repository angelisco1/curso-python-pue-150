from flask import Flask
from api.controllers import ingredients_bp

app = Flask(__name__)

app.register_blueprint(ingredients_bp)

if __name__ == "__main__":
    app.run(debug=True, port=3006)

