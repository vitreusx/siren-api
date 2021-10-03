from graphene import *
from .source import Source
from siren import models


class Track(ObjectType):
    id = NonNull(ID)
    name = NonNull(String)
    source = NonNull(Source)
    start_sec = Float()
    end_sec = Float()

    def resolve_id(root: models.Track, info):
        return root.id

    def resolve_name(root: models.Track, info):
        return root.name

    def resolve_source(root: models.Track, info):
        return root.source

    def resolve_start_sec(root: models.Track, info):
        return root.start_sec

    def resolve_end_sec(root: models.Track, info):
        return root.end_sec
