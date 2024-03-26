from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

def create_app():
    from routes import routes_bp
    app.register_blueprint(routes_bp)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
