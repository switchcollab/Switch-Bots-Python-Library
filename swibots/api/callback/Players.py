from swibots.utils.types import JSONDict
from typing import Dict, Any, Optional
from .types import Component, Icon


class VideoPlayer(Component):
    type = "video_player"

    def __init__(self, url: str, title: str = "", subtitle: str = ""):
        self.url = url
        self.title = title
        self.subtitle = subtitle

    def to_json(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "url": self.url,
            "title": self.title,
            "subtitle": self.subtitle,
        }


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
