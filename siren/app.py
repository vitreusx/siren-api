from flask import Flask
from . import auth, graphql
from .models.db import db
from dotenv import load_dotenv
import os


def create_app() -> Flask:
    app = Flask(__name__)

    load_dotenv()
    app.config.from_mapping(
        {
            "DB_NAME": "siren",
            "DB_USERNAME": os.getenv("MONGO_INITDB_ROOT_USERNAME"),
            "DB_PASSWORD": os.getenv("MONGO_INITDB_ROOT_PASSWORD"),
            "DB_HOST": "db",
            "DB_PORT": 27017,
            "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID"),
            "SPOTIFY_CLIENT_SECRET": os.getenv("SPOTIFY_CLIENT_SECRET"),
        }
    )
    app.secret_key = os.getenv("FLASK_SECRET")

    db.init_app(app)
    auth.init_app(app)
    app.register_blueprint(auth.router, url_prefix="/auth")
    app.register_blueprint(graphql.router, url_prefix="/graphql")

    return app
