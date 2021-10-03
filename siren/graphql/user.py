from graphene import *
from .track import Track
from siren import models


class User(ObjectType):
    id = NonNull(ID)
    username = NonNull(String)
    sf_access_token = String()
    tracks = List(NonNull(Track))

    def resolve_id(root: models.User, info):
        return root.id

    def resolve_username(root: models.User, info):
        return root.auth.username

    def resolve_sf_access_token(root: models.User, info):
        if not root.sf_auth:
            return None
        else:
            return root.sf_auth.access_token

    def resolve_tracks(root: models.User, info):
        return root.tracks
