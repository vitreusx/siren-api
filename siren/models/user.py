from mongoengine import Document, DENY, NULLIFY
from mongoengine.fields import *
from .user_auth import UserAuth
from .sf_auth import SfAuth
from flask_login import UserMixin
from .track import Track


class User(Document, UserMixin):
    auth = EmbeddedDocumentField(UserAuth, required=True)
    sf_auth = EmbeddedDocumentField(SfAuth)
    tracks = ListField(ReferenceField(Track), default=list)
