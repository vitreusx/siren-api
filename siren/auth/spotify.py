from flask import Blueprint, request, redirect, session, current_app
from flask.helpers import url_for
from flask_login import current_user
from flask_login.utils import login_required
import secrets
import requests
from urllib.parse import urlencode
import os
import time

from siren import models
from siren.models.sf_auth import SfAuth

router = Blueprint("spotify", __name__)


@router.route("/login", methods=["POST"])
@login_required
def login():
    scopes = [
        "app-remote-control",
        "streaming",
        "user-read-playback-state",
        "user-modify-playback-state",
        "user-read-currently-playing",
        "user-library-read",
        "user-read-email",
        "user-read-private",
    ]
    state = secrets.token_urlsafe(32)
    session["state"] = state
    redirect_uri = f"{request.form.get('server_url')}{url_for('.callback')}"
    session["sf_redirect_uri"] = redirect_uri

    params = {
        "response_type": "code",
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "scope": " ".join(scopes),
        "redirect_uri": redirect_uri,
        "state": state,
    }
    url = f"https://accounts.spotify.com/authorize/?{urlencode(params)}"
    
    return redirect(url)


@router.route("/callback")
@login_required
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if state != session.get("state"):
        return "State token doesn't match!", 500

    redirect_uri = session.get("sf_redirect_uri")
    print(f"redirect_uri = {redirect_uri}")

    data = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET"),
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    url = "https://accounts.spotify.com/api/token"
    response = requests.post(url, headers=headers, data=data).json()
    print(f"response = {response}")

    # TODO validate, check status code

    current_user.sf_auth = SfAuth(
        access_token=response["access_token"],
        refresh_token=response["refresh_token"],
        expires_at=int(time.time()) + response["expires_in"],
        scope=response["scope"],
    )
    current_user.save()

    return redirect(session["sf_login_redirect"])


@router.route("/logout", methods=["POST"])
@login_required
def logout():
    user = models.User.objects(id=current_user.id)
    user.update_one(unset__sf_auth=True)
    current_user.save()
    return redirect(request.form.get("redirect"))
