from graphene import *
from .track import Track
from urllib.parse import urlparse
from pathlib import Path
from siren import models


class AddYtTrackInput(InputObjectType):
    user_id = NonNull(ID)
    title = NonNull(String)
    video_url = NonNull(String)


class AddYtTrack(Mutation):
    class Arguments:
        input = NonNull(AddYtTrackInput)

    Output = Track

    @staticmethod
    def get_source_model(video_url: str) -> models.Source:
        audio = models.YtAudio.objects(video_url=video_url).first()
        if audio is None:
            audio = models.YtAudio(video_url=video_url).save()
        return audio

    def mutate(root, info, input: AddYtTrackInput):
        user = models.User.objects(id=input.user_id).first()
        if user is None:
            return

        source = AddYtTrack.get_source_model(input.video_url)
        track = models.Track(title=input.title, source=source).save()

        user.tracks.append(track)
        user.save()

        return track
