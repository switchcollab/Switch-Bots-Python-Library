from swibots.utils.types import JSONDict
from .types import Image, Component, Layout
from typing import List, Any


class Carousel(Layout):
    type = "carousel"

    def __init__(
        self,
        images: List[Image],
        title: str = "",
        subtitle: str = "",
    ):
        self.title = title
        self.subtitle = subtitle
        self.images = images

    def to_json(self):
        data = {
            "type": self.type,
            "components": [image.to_json() for image in self.images],
            "title": self.title,
            "subTitle": self.subtitle,
        }
        return data
