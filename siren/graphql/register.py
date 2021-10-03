from graphene import *
from .user import User
from .user_auth_input import UserAuthInput
from siren import models


class Register(Mutation):
    class Arguments:
        input = NonNull(UserAuthInput)

    Output = NonNull(User)

    def mutate(root, info, input: UserAuthInput):
        auth = models.UserAuth.create(input.username, input.password)
        user = models.User(auth=auth).save()
        return user
