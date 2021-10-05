from graphene import *
from siren import models


class SfTrack(ObjectType):
    id = NonNull(ID)
    track_id = NonNull(String)

    def resolve_id(root: models.SfTrack, info):
        return root.id

    def resolve_track_id(root: models.SfTrack, info):
        return root.track_id
