from flask import Flask
from mongoengine import connect


class Database:
    def __init__(self, app: Flask = None) -> None:
        self.app = app
        if app is not None:
            self.init_app(self.app)

    def init_app(self, app: Flask = None) -> None:
        connect(
            db="orpheus",
            username="root",
            password="root",
            authentication_source="admin",
            host="mongodb://mongo:27017",
        )


db = Database()
