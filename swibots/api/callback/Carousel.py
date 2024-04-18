from swibots.utils.types import JSONDict
from .types import Image, Component
from typing import List, Any


class Carousel(Component):
    type = "carousel"

    def __init__(
        self,
        images: List[Image],
        title: str = "",
        subtitle: str = "",
        max_size: bool = None
    ):
        self.title = title
        self.subtitle = subtitle
        self.images = images
        self.max_size = max_size

    def to_json(self):
        data = {
            "type": self.type,
            "components": [image.to_json() for image in self.images],
            "title": self.title,
            "subTitle": self.subtitle,
            "mainAxisSize": "max" if self.max_size else "min"
        }
        return data
