from mongoengine import connect, Document
from mongoengine.connection import disconnect
from mongoengine.fields import *
from flask import Flask


class Database:
    def __init__(self, app: Flask = None):
        if app:
            self.init_app(app)

    def _connect(self):
        self.conn = connect(
            db=self.app.config.get("DB_NAME"),
            username=self.app.config.get("DB_USER"),
            password=self.app.config.get("DB_PASSWORD"),
            host=self.app.config.get("DB_HOST"),
            port=int(self.app.config.get("DB_PORT")),
            authentication_source="admin",
        )

    def init_app(self, app: Flask):
        self.app = app
        self._connect()

    def clear(self):
        db_name = self.app.config.get("DB_NAME")
        self.conn.drop_database(db_name)
        disconnect()
        self._connect()


db = Database()
