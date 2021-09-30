from flask import Blueprint, request
from werkzeug.utils import redirect
from flask_login import LoginManager, current_user, login_user
from flask_login.utils import login_required, logout_user
from siren.models.db import db
from siren.models.user_auth import UserAuth
from http import HTTPStatus

router = Blueprint("user", __name__)
lm = LoginManager()


@lm.user_loader
def load_user(user_id):
    return UserAuth.objects.get(id=user_id)


@router.route("/status")
def status():
    logged_in = current_user.is_authenticated
    username = current_user.username if logged_in else None
    return {"logged_in": logged_in, "username": username}


@router.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    redirect_uri = request.form.get("redirect")

    try:
        user = UserAuth.create(username, password)
        user.save()
        return redirect(redirect_uri)
    except:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT


@router.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = request.form.get("remember")
    redirect_uri = request.form.get("redirect")

    user = UserAuth.objects.get(username=username)
    if user and user.verify(password):
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
