from graphene import *
from .user import User
from .source import Source
from .user_auth_input import UserAuthInput
from siren import models
from flask_login import current_user


class Query(ObjectType):
    me = Field(User)
    user = Field(User, input=NonNull(UserAuthInput))
    users = List(NonNull(User))
    sources = List(NonNull(Source))

    def resolve_me(root, info) -> models.User:
        if current_user.is_authenticated:
            return current_user

    def resolve_user(root, info, input) -> models.User:
        return models.User.objects(auth__username=input.username).first()

    def resolve_users(root, info) -> list[models.User]:
        return models.User.objects

    def resolve_sources(root, info) -> list[models.Source]:
        return models.Source.objects
