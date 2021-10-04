from graphene import *
from .track import Track
from siren import models


class AddTrackInput(InputObjectType):
    user_id = NonNull(ID)
    name = NonNull(String)
    source_id = NonNull(ID)
    start_sec = Float()
    end_sec = Float()


class AddTrack(Mutation):
    class Arguments:
        input = NonNull(AddTrackInput)

    Output = Track

    def mutate(root, info, input: AddTrackInput):
        source = models.Source.objects(id=input.source_id).first()
        if source is None:
            return

        user = models.User.objects(id=input.user_id).first()
        if user is None:
            return

        track = models.Track(
            name=input.name,
            source=source,
            start_sec=input.start_sec,
            end_sec=input.end_sec,
        )
        track.save()

        user.tracks.append(track)
        user.save()

        return track
