from graphene import *
from .sf_track import SfTrack
from .yt_audio import YtAudio
from siren import models


class Source(Union):
    class Meta:
        types = [SfTrack, YtAudio]

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, models.SfTrack):
            return SfTrack
        elif isinstance(instance, models.YtAudio):
            return YtAudio
        else:
            return super().resolve_type(instance, info)
