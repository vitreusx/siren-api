from flask import Flask
from mongoengine import connect


class Database:
    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(self.app)

    def init_app(self, app: Flask) -> None:
        self.app = app
        host = app.config.get("DB_HOST")
        port = app.config.get("DB_PORT")

        connect(
            db=app.config.get("DB_NAME"),
            username=app.config.get("DB_USERNAME"),
            password=app.config.get("DB_PASSWORD"),
            authentication_source="admin",
            host=f"mongodb://{host}:{port}",
        )


db = Database()
