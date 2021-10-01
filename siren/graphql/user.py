from graphene.types import *
from siren.models.user_auth import UserAuth


class User(ObjectType):
    id = NonNull(ID)
    username = NonNull(String)
    sf_access_token = String()

    def resolve_id(parent, info):
        return parent.get_id()

    def resolve_username(parent, info):
        return UserAuth.objects.get(id=parent.get_id()).username

    def resolve_sf_auth_token(parent, info):
        id = parent.resolve_id(info)
        user = UserAuth.objects.get(id=parent.get_id())
        if user.sf_auth:
            return user.sf_auth.access_token
