from graphene import *


class UserAuthInput(InputObjectType):
    username = NonNull(String)
    password = NonNull(String)
