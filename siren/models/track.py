from mongoengine import Document
from mongoengine.fields import *
from mongoengine.queryset.base import DENY
from .source import Source


class Track(Document):
    title = StringField(required=True)
    source = ReferenceField(Source, required=True)
