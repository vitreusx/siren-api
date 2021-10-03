from .source import Source
from mongoengine.fields import *


class SfSource(Source):
    name = StringField(required=True)
    spotify_uri = StringField(required=True)
