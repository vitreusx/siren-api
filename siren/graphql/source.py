from graphene import *
from .sf_source import SfSource
from .yt_source import YtSource
from siren import models


class Source(Union):
    class Meta:
        types = [SfSource, YtSource]

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, models.SfSource):
            return SfSource
        elif isinstance(instance, models.YtSource):
            return YtSource
        else:
            return super().resolve_type(instance, info)
