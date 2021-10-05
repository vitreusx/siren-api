from flask import Blueprint, request
from werkzeug.utils import redirect
from flask_login import LoginManager, current_user, login_user
from flask_login.utils import login_required, logout_user
from siren.models.db import db
from siren.models.user import User, UserAuth
from http import HTTPStatus

router = Blueprint("user", __name__)
lm = LoginManager()


@lm.user_loader
def user_loader(id):
    return User.objects(id=id).first()


@router.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    redirect_uri = request.form.get("redirect")

    if User.objects(auth__username=username).count() > 0:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT
    else:
        user_auth = UserAuth.create(username, password)
        user = User(auth=user_auth, tracks=[]).save()
        return redirect(redirect_uri)


@router.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = request.form.get("remember")
    redirect_uri = request.form.get("redirect")

    user: User = User.objects(auth__username=username).first()
    if user and user.auth and user.auth.verify(password):
        login_user(user, remember=remember)
        return redirect(redirect_uri)
    else:
        return {"error": "Wrong credentials."}, HTTPStatus.UNAUTHORIZED


@router.route("/logout", methods=["POST"])
@login_required
def logout():
    redirect_url = request.form.get("redirect")
    if current_user.is_authenticated:
        logout_user()
        return redirect(redirect_url)
    else:
        return {"error": "Not logged in"}, HTTPStatus.BAD_REQUEST
