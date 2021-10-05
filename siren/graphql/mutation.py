import graphene
from .register import Register
from .add_sf_track import AddSfTrack
from .add_yt_track import AddYtTrack
from .remove_track import RemoveTrack
from .clear_all import ClearAll


class Mutation(graphene.ObjectType):
    register = Register.Field()
    add_sf_track = AddSfTrack.Field()
    add_yt_track = AddYtTrack.Field()
    remove_track = RemoveTrack.Field()
    clear_all = ClearAll.Field()
