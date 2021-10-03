from graphene import *
from .yt_source import YtSource
from siren import models


class AddYtSourceInput(InputObjectType):
    name = String()
    video_url = NonNull(String)


class AddYtSource(Mutation):
    class Arguments:
        input = NonNull(AddYtSourceInput)

    Output = NonNull(YtSource)

    def mutate(root, info, input: AddYtSourceInput):
        name = input.name or models.YtSource.video_title(input.video_url)
        yt_source = models.YtSource(name=name, video_url=input.video_url).save()
        return yt_source
