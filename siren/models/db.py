from mongoengine import connect, Document
from mongoengine.fields import *
from flask import Flask


class Database:
    def __init__(self, app: Flask = None):
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.app = app

        connect(
            db=app.config.get("DB_NAME"),
            username=app.config.get("DB_USER"),
            password=app.config.get("DB_PASSWORD"),
            host=app.config.get("DB_HOST"),
            port=int(app.config.get("DB_PORT")),
            authentication_source="admin",
        )


db = Database()
