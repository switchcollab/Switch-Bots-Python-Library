from typing import Union, List

from swibots.utils.types import JSONDict
from .types import Layout, Image, Component


class Card(Layout):
    type = "card"

    def __init__(
        self,
        title: str,
        subtitle: str = "",
        image: Union[Image, str] = None,
        actions: List[Component] = [],
    ):
        self.title = title
        self.subtitle = subtitle
        if isinstance(image, str):
            image = Image(image)
        self.image = image
        self.actions = actions
        
    def to_json(self):
        return {
            "type": self.type,
            "title": self.title,
            "subTitle": self.subtitle,
            "image": self.image.to_json(),
            "components": [
                action.to_json() for action in self.actions
            ]
        }