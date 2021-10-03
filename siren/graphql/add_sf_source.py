from graphene import *
from .sf_source import SfSource
from siren import models


class AddSfSourceInput(InputObjectType):
    name = String()
    spotify_uri = NonNull(String)


class AddSfSource(Mutation):
    class Arguments:
        input = NonNull(AddSfSourceInput)

    Output = NonNull(SfSource)

    def mutate(root, info, input: AddSfSourceInput):
        sf_source = models.SfSource(
            name=input.name, spotify_uri=input.spotify_uri
        ).save()
        return sf_source
