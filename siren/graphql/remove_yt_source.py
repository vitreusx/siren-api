from graphene import *
from siren import models


class RemoveYtSourceInput(InputObjectType):
    id = NonNull(ID)


class RemoveYtSource(Mutation):
    class Arguments:
        input = NonNull(RemoveYtSourceInput)

    Output = NonNull(Boolean)

    def mutate(root, info, input: RemoveYtSourceInput):
        yt_source = models.YtSource.objects(id=id).first()
        if yt_source:
            yt_source.delete()
            return True
        else:
            return False
