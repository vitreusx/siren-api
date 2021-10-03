from graphene import *
from siren import models


class RemoveSfSourceInput(InputObjectType):
    id = NonNull(ID)


class RemoveSfSource(Mutation):
    class Arguments:
        input = NonNull(RemoveSfSourceInput)

    Output = NonNull(Boolean)

    def mutate(root, info, input: RemoveSfSourceInput):
        sf_source = models.SfSource.objects(id=id).first()
        if sf_source:
            sf_source.delete()
            return True
        else:
            return False
