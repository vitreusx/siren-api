from __future__ import annotations
from mongoengine import EmbeddedDocument
from mongoengine.fields import *
import bcrypt


class UserAuth(EmbeddedDocument):
    username = StringField(required=True, max_length=64)
    salt = StringField(required=True, max_length=29)
    hash = StringField(required=True, max_length=60)

    @staticmethod
    def create(username: str, password: str) -> UserAuth:
        salt = bcrypt.gensalt().decode("utf-8")
        hash = bcrypt.hashpw(password.encode(), salt.encode()).decode("utf-8")
        return UserAuth(username=username, salt=salt, hash=hash)

    def verify(self, password: str) -> bool:
        hash = bcrypt.hashpw(password.encode(), self.salt.encode())
        return hash == self.hash.encode()
