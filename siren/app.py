from flask import Flask
from . import auth, graphql
from .models.db import db
from dotenv import load_dotenv
import os


def create_app() -> Flask:
    app = Flask(__name__)

    load_dotenv()

    class Config:
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
        SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

    app.config.from_object(Config)
    app.secret_key = os.getenv("FLASK_SECRET")

    db.init_app(app)

    auth.init_app(app)

    app.register_blueprint(auth.router, url_prefix="/auth")
    app.register_blueprint(graphql.router, url_prefix="/graphql")

    return app
