from graphene import *
from .source import Source
from siren import models


class Track(ObjectType):
    id = NonNull(ID)
    title = NonNull(String)
    source = NonNull(Source)

    def resolve_id(root: models.Track, info):
        return root.id

    def resolve_title(root: models.Track, info):
        return root.title

    def resolve_source(root: models.Track, info):
        return root.source
