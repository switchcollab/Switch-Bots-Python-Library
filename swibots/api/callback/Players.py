from swibots.utils.types import JSONDict
from typing import Dict, Any, Optional, Union, List
from .types import Component, Image, Badge


class AudioPlayer(Component):
    type = "audio_player"

    def __init__(
        self,
        title: str,
        url: str,
        subtitle: str = "",
        thumb: Union[Image, str] = None,
    ):
        self.title = title
        self.url = url
        self.subtitle = subtitle
        self.thumb = thumb

    def to_json(self):
        return {
            "type": self.type,
            "title": self.title,
            "subtitle": self.subtitle,
            "image": self.thumb.to_json(),
            "url": self.url,
        }


class VideoPlayer(Component):
    type = "video_player"

    def __init__(
        self,
        url: str,
        title: str = "",
        subtitle: str = "",
        full_screen: bool = False,
        badges: List[Badge] = None,
    ):
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.full_screen = full_screen
        self.badges = badges

    def to_json(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "url": self.url,
            "title": self.title,
            "subtitle": self.subtitle,
            "fullScreen": self.full_screen,
        }
        if self.badges:
            data["badges"] = [badge.to_json() for badge in self.badges]
        return data


class Embed(Component):
    type = "embed"

    def __init__(
        self,
        url: str,
        height: Optional[int] = 0,
        width: Optional[int] = 0,
        full_screen: Optional[bool] = True,
    ):
        self.url = url
        self.height = height
        self.width = width
        self.full_screen = full_screen

    def to_json(self):
        return {
            "type": self.type,
            "url": self.url,
            "height": self.height,
            "width": self.width,
            "fullScreen": self.full_screen,
        }


class FileViewer(Component):
    type = "pdf_viewer"

    def __init__(self, url: str):
        self.url = url

    def to_json(self):
        return {"type": self.type, "url": self.url}
