from graphene import *
from siren import models


class RemoveTrackInput(InputObjectType):
    user_id = NonNull(ID)
    track_id = NonNull(ID)


class RemoveTrack(Mutation):
    class Arguments:
        input = NonNull(RemoveTrackInput)

    Output = NonNull(Boolean)

    def mutate(root, info, input: RemoveTrackInput):
        user = models.User.objects(id=input.user_id).first()
        if user is None:
            return False

        track = models.Track.objects(id=input.track_id).first()
        if track is None:
            return False

        track.delete()
        return True
