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
        user_qs = models.User.objects(id=input.user_id)
        if not user_qs.first():
            return False

        num_updated = user_qs.update_one(pull__tracks__id=input.track_id)
        return num_updated > 0
