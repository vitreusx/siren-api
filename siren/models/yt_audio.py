from __future__ import annotations
from .source import Source
from mongoengine.fields import *
from youtube_dl import YoutubeDL
from datetime import datetime
from urllib.parse import urlparse, parse_qs


class YtAudio(Source):
    video_url = URLField(required=True, unique=True)
    stream_url = URLField()
    expires_at = DateTimeField()

    _opts = {"format": "bestaudio", "quiet": True, "no_warnings": True}

    @staticmethod
    def video_title(video_url: str) -> str:
        with YoutubeDL(YtAudio._opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info["title"]

    def _need_refetch(self):
        if self.stream_url is None:
            return True
        elif self.expires_at is not None and self.expires_at <= datetime.now():
            return True
        else:
            return False

    def refetch_stream(self):
        if self._need_refetch():
            with YoutubeDL(YtAudio._opts) as ydl:
                info = ydl.extract_info(self.video_url, download=False)

                bestaudio = max(info["formats"], key=lambda fmt: fmt.get("abr", 0))

                self.stream_url = bestaudio["url"]
                url_qs = urlparse(self.stream_url).query
                expire_unix = int(parse_qs(url_qs)["expire"][0])
                self.expires_at = datetime.fromtimestamp(expire_unix)

                self.save()
