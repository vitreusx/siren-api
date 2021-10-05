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
        query_set = models.User.objects(id=input.user_id)
        if not query_set.first():
            return False

        num_updated = query_set.update_one(pull__tracks__id=input.track_id)
        return num_updated > 0
