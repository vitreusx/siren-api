from graphene import *
from siren.models.db import db


class ClearAll(Mutation):
    Output = NonNull(Boolean)

    def mutate(root, info):
        db.clear()
        return True
