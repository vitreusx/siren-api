from mongoengine import Document
from mongoengine.fields import *


class Source(Document):
    meta = {"allow_inheritance": True}
