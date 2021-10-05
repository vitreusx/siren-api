from graphene import *
from siren import models
from urllib.parse import urlparse
from pathlib import Path


class SfTrackInput(ObjectType):
    track_link = NonNull(String)

    def get_source(self) -> models.Source:
        path = urlparse(self.track_link).path
        track_id = Path(path).parts[-1]

        track = models.SfTrack.objects(track_id=track_id).first()
        if not track:
            track = models.SfTrack(track_id=track_id).save()

        return track


class YtAudioInput(ObjectType):
    video_url = NonNull(String)

    def get_source(self) -> models.Source:
        audio = models.YtAudio.objects(video_url=self.video_url).first()
        return audio


class SourceInput(Union):
    class Meta:
        types = [SfTrackInput, YtAudioInput]

    @classmethod
    def resolve_type(cls, instance, info):
        # TODO do it properly
        if hasattr(instance, "track_link"):
            return SfTrackInput
        elif hasattr(instance, "video_url"):
            return YtAudioInput
        else:
            return super().resolve_type(instance, info)
