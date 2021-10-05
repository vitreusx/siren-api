from mongoengine import EmbeddedDocument
from mongoengine.fields import *
from mongoengine.queryset.base import DENY
from bson.objectid import ObjectId
from .source import Source


class Track(EmbeddedDocument):
    id = ObjectIdField(
        required=True,
        default=ObjectId,
        unique=True,
    )
    title = StringField(required=True)
    source = ReferenceField(Source, required=True)
