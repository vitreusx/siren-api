from flask import Blueprint, request, redirect, session
from flask.helpers import url_for
from flask_login import current_user
from flask_login.utils import login_required
import secrets
import requests
from urllib.parse import urlencode
import os
import time

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from siren.models.sf_auth import SpotifyAuth

router = Blueprint("spotify", __name__)


@router.route("/token")
@login_required
def token():
    if current_user.sf_auth:
        client: Spotify = current_user.sf_auth.client
        oauth: SpotifyOAuth = client.oauth_manager
        return {"token": oauth.get_access_token()["access_token"]}
    else:
        return {}


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
    ]
    state = secrets.token_urlsafe(32)  # TODO save it for later checking
    redirect_uri = f"http://localhost:8000{url_for('.callback')}"
    session["sf_login_redirect"] = request.form.get("redirect")

    params = {
        "response_type": "code",
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "scope": " ".join(scopes),
        "redirect_uri": redirect_uri,
        "state": state,
    }
    url = f"https://accounts.spotify.com/authorize/?{urlencode(params)}"

    # TODO finish it tomorrow; /callback should redirect to the original page,
    # this particular request is actually fairly regular in that regard
    return redirect(url)


@router.route("/callback")
@login_required
def callback():
    code = request.args.get("code")
    redirect_uri = f"http://localhost:8000{url_for('.callback')}"
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
    # TODO validate, check status code

    auth = SpotifyAuth(
        access_token=response["access_token"],
        refresh_token=response["refresh_token"],
        expires_at=int(time.time()) + response["expires_in"],
        scope=response["scope"],
    )
    auth.save()

    current_user.sf_auth = auth
    current_user.save()

    return redirect(session["sf_login_redirect"])


@router.route("/logout", methods=["POST"])
@login_required
def logout():
    current_user.sf_auth.delete()
    current_user.save()
    return redirect(request.form.get("redirect"))
