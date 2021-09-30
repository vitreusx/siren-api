from flask import Flask, Blueprint
from . import user, spotify


def init_app(app: Flask):
    user.lm.init_app(app)


router = Blueprint("auth", __name__)
router.register_blueprint(user.router, url_prefix="/user")
router.register_blueprint(spotify.router, url_prefix="/spotify")
