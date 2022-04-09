from flask import Flask
from dotenv import load_dotenv
from app import blueprints

def create_app():
    app = Flask(__name__)

    load_dotenv()

    blueprints.init_app(app) # <- inicializar as rotas/blueprints

    return app