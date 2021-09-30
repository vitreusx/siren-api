from __future__ import annotations
from mongoengine import Document
from mongoengine.fields import StringField, IntField
from spotipy import Spotify
from spotipy.oauth2 import CacheHandler, SpotifyClientCredentials, SpotifyOAuth
from flask import url_for, current_app
import os


class SpotifyAuthCache(CacheHandler):
    def __init__(self, sf_auth: SpotifyAuth) -> None:
        super().__init__()
        self.sf_auth = sf_auth

    def get_cached_token(self):
        return self.sf_auth.token_info

    def save_token_to_cache(self, token_info):
        self.sf_auth.access_token = token_info["access_token"]
        self.sf_auth.refresh_token = token_info["refresh_token"]
        self.sf_auth.expires_at = token_info["expires_at"]
        self.sf_auth.scope = token_info["scope"]
        self.sf_auth.save()


class SpotifyAuth(Document):
    access_token = StringField()
    refresh_token = StringField()
    expires_at = IntField()
    scope = StringField()

    @property
    def token_info(self):
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
            "scope": self.scope,
        }

    @property
    def client(self):
        oauth = SpotifyOAuth(
            redirect_uri=url_for("api.spotify.callback"),
            cache_handler=SpotifyAuthCache(self),
            scope="user-library-read",
            client_id=current_app.config.get("SPOTIFY_CLIENT_ID"),
            client_secret=current_app.config.get("SPOTIFY_CLIENT_SECRET"),
        )
        return Spotify(oauth_manager=oauth)
