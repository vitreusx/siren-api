from graphene.types import *
from .user import User
from flask_login import current_user


class Query(ObjectType):
    me = Field(User)

    def resolve_me(parent, info):
        if current_user.is_authenticated:
            return current_user
        else:
            return None
