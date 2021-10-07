from .source import Source
from mongoengine.fields import *


class SfTrack(Source):
    track_id = StringField(required=True)
