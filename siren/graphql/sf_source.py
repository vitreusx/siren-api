from graphene import *
from siren import models


class SfSource(ObjectType):
    id = NonNull(ID)
    spotify_uri = NonNull(String)

    def resolve_id(root: models.SfSource, info):
        return root.id

    def resolve_spotify_uri(root: models.SfSource, info):
        return root.spotify_uri
