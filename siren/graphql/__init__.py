from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

router = Blueprint("graphql", __name__)

router.add_url_rule(
    "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

router.add_url_rule(
    "/batch",
    view_func=GraphQLView.as_view("graphql_batch", schema=schema, batch=True),
)
