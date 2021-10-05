from graphene import *
from .track import Track
from urllib.parse import urlparse
from pathlib import Path
from siren import models


class AddSfTrackInput(InputObjectType):
    user_id = NonNull(ID)
    title = NonNull(String)
    track_link = NonNull(String)


class AddSfTrack(Mutation):
    class Arguments:
        input = NonNull(AddSfTrackInput)

    Output = Track

    @staticmethod
    def get_source_model(track_link: str) -> models.Source:
        path = urlparse(track_link).path
        track_id = Path(path).parts[-1]

        track = models.SfTrack.objects(track_id=track_id).first()
        if not track:
            track = models.SfTrack(track_id=track_id).save()

        return track

    def mutate(root, info, input: AddSfTrackInput):
        user = models.User.objects(id=input.user_id).first()
        if user is None:
            return

        source = AddSfTrack.get_source_model(input.track_link)
        track = user.tracks.create(title=input.title, source=source)
        user.save()

        return track
