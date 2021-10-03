import graphene
from .register import Register
from .add_sf_source import AddSfSource
from .remove_sf_source import RemoveSfSource
from .add_yt_source import AddYtSource
from .remove_yt_source import RemoveYtSource
from .add_track import AddTrack
from .remove_track import RemoveTrack


class Mutation(graphene.ObjectType):
    register = Register.Field()
    add_sf_source = AddSfSource.Field()
    remove_sf_source = RemoveSfSource.Field()
    add_yt_source = AddYtSource.Field()
    remove_yt_source = RemoveYtSource.Field()
    add_track = AddTrack.Field()
    remove_track = RemoveTrack.Field()
