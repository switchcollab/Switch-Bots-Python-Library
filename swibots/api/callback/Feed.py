from typing import List
from .types import Component, Icon, Any, Dict


class ShortVideo(Component):
    type = "short_video"

    def __init__(
        self,
        url: str = None,
        icons: List[Icon] = None,
        user_image: str = None,
        user_name: str = None,
        title: str = None,
        description: str = None,
    ):
        self.url = url
        self.icons = icons
        self.user_image = user_image
        self.user_name = user_name
        self.title = title
        self.description = description

    def to_json(self):
        data = {
            "type": "short_video",
            "videoUrl": self.url,
            "bottom": [icon.to_json() for icon in self.icons],
            "extraOptions": {
                "userAvatar": self.user_image,
                "userName": self.user_name,
                "description": self.description,
                "title": self.title,
            },
        }
        return data


class FeedPanel(Component):
    def __init__(self, feeds, next_callback: str):
        self.feeds = feeds
        self.next_callback = next_callback

    def to_json(self) -> Dict[str, Any]:
        data = {
            "type": "feed_panel",
            "feeds": [feed.to_json() for feed in self.feeds],
            "offsetCallbackData": self.next_callback,
        }
        return data
