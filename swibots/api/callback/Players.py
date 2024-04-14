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
        id: str = None,
        callback_data: str = None,
        previous_callback: Optional[str] = "",
        next_callback: Optional[str] = "",
        max_size: bool = False
    ):
        self.title = title
        self.url = url
        self.id = id
        self.subtitle = subtitle
        self.thumb = thumb
        self.callback_data = callback_data
        self.previous_callback = previous_callback
        self.next_callback = next_callback
        self.max_size=  max_size

    def to_json(self):
        return {
            "type": self.type,
            "title": self.title,
            "subtitle": self.subtitle,
            "image": self.thumb.to_json(),
            "url": self.url,
            "songId": self.id,
            "onSongUpdate": self.callback_data,
            "previousCallback": self.previous_callback,
            "nextCallback": self.next_callback,
            "mainAxisSize": "max" if self.max_size else "min"
        }


class VideoPlayer(Component):
    type = "video_player"

    def __init__(
        self,
        url: str,
        title: str = "",
        subtitle: str = "",
        id: str = "",
        full_screen: bool = False,
        badges: List[Badge] = None,
        callback_data: str = None,
            max_size: bool = False
    
    ):
        self.url = url
        self.title = title
        self.id = id
        self.subtitle = subtitle
        self.full_screen = full_screen
        self.badges = badges
        self.callback_data = callback_data
        self.max_size=  max_size

    def to_json(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "url": self.url,
            "videoId": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "fullScreen": self.full_screen,
            "mainAxisSize": "max" if self.max_size else "min"
        }
        if self.callback_data:
            data["onVideoUpdate"] = self.callback_data
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
        allow_navigation: bool = False,
        navigation_callback: str = None,
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
        self.navigation_callback = navigation_callback
        self.__kwargs = kwargs

    def to_json(self):
        data = {
            "type": self.type,
            "url": self.url,
            "height": self.height,
            "width": self.width,
            "fullScreen": self.full_screen,
            "extraOptions": {
                **self.__kwargs
                },
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
        if self.navigation_callback:
            data["extraOptions"]["navigationCallback"] = self.navigation_callback
        return data


class FileViewer(Component):
    type = "pdf_viewer"

    def __init__(self, url: str):
        self.url = url

    def to_json(self):
        return {"type": self.type, "url": self.url}
