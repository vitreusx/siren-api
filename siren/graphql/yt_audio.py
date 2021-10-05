from graphene import *
from siren import models


class YtAudio(ObjectType):
    id = NonNull(ID)
    video_url = NonNull(String)
    stream_url = NonNull(String)
    expires_at = NonNull(Date)

    def resolve_id(root: models.YtAudio, info):
        root.refetch_stream()
        return root.id

    def resolve_video_url(root: models.YtAudio, info):
        root.refetch_stream()
        return root.video_url

    def resolve_stream_url(root: models.YtAudio, info):
        root.refetch_stream()
        return root.stream_url

    def resolve_expires_at(root: models.YtAudio, info):
        root.refetch_stream()
        return root.expires_at
