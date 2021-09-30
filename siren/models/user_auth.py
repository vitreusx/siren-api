from __future__ import annotations
from typing import Optional
from mongoengine import Document
from flask_login import UserMixin
import bcrypt
from mongoengine.fields import StringField, ReferenceField
from mongoengine.queryset.base import NULLIFY
from .sf_auth import SpotifyAuth


class UserAuth(UserMixin, Document):
    username = StringField(max_length=64, unique=True)
    salt = StringField(max_length=29)
    hash = StringField(max_length=60)

    sf_auth = ReferenceField(SpotifyAuth, reverse_delete_rule=NULLIFY)

    @staticmethod
    def create(username: str, password: str) -> UserAuth:
        salt = bcrypt.gensalt().decode("utf-8")
        hash = bcrypt.hashpw(password.encode(), salt.encode()).decode("utf-8")
        return UserAuth(username=username, salt=salt, hash=hash)

    def verify(self, password: str) -> bool:
        hash = bcrypt.hashpw(password.encode(), self.salt.encode())
        return hash == self.hash.encode()
