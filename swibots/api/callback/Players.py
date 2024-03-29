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
        previous_callback: Optional[str] = "",
        next_callback: Optional[str] = "",
    ):
        self.title = title
        self.url = url
        self.subtitle = subtitle
        self.thumb = thumb
        self.previous_callback = previous_callback
        self.next_callback = next_callback

    def to_json(self):
        return {
            "type": self.type,
            "title": self.title,
            "subtitle": self.subtitle,
            "image": self.thumb.to_json(),
            "url": self.url,
            "previousCallback": self.previous_callback,
            "nextCallback": self.next_callback,
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
        expand: Optional[bool] = False,
        full_screen: Optional[bool] = True,
        proxy: Optional[dict] = None,
        landscape: bool = False,
        allow_navigation: bool = True,
        enable_ads: bool = False,
        view_ratio: int = None,
        **kwargs
    ):
        self.url = url
        self.height = height
        self.width = width
        self.full_screen = full_screen
        self.expand = expand
        self.proxy = proxy
        self.landscape = landscape
        self.view_ratio = view_ratio
        self.enable_ads = enable_ads
        self.allow_navigation = allow_navigation
        self.__kwargs = kwargs

    def to_json(self):
        data = {
            "type": self.type,
            "url": self.url,
            "height": self.height,
            "width": self.width,
            "fullScreen": self.full_screen,
            "extraOptions": {**self.__kwargs},
        }
        if self.expand:
            data["expansion"] = "flexible_expansion"
        if self.proxy:
            data["proxy"] = self.proxy
        if self.landscape:
            data["extraOptions"]["orientation"] = "landscape"
        if self.allow_navigation:
            data["extraOptions"]["navigation"] = self.allow_navigation
        if self.view_ratio:
            data["extraOptions"]["viewRatio"] = self.view_ratio
        if self.enable_ads:
            data["extraOptions"]["enableAds"] = self.enable_ads
        return data


class FileViewer(Component):
    type = "pdf_viewer"

    def __init__(self, url: str):
        self.url = url

    def to_json(self):
        return {"type": self.type, "url": self.url}
