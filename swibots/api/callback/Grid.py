from swibots.utils.types import JSONDict
from .types import Layout, SwitchObject, Expansion
from typing import List, Optional


class GridItem(SwitchObject):
    def __init__(
        self,
        title: str,
        media: str,
        subtitle: str = "",
        callback_data: str = None,
        selective: bool = False,
    ):
        self.title = title
        self.subtitle = subtitle
        self.media = media
        self.callback_data = callback_data
        self.selective = selective

    def to_json(self) -> JSONDict:
        return {
            "selective": self.selective,
            "title": self.title,
            "subTitle": self.subtitle,
            "media": self.media,
            "callbackData": self.callback_data,
        }


class Grid(Layout):
    type = "grid"

    def __init__(
        self,
        title: str = None,
        horizontal: bool = False,
        options: List[GridItem] = None,
        size: int = 3,
        expansion: Optional[Expansion] = Expansion.DEFAULT,
    ):
        self.size = size
        self.options = options
        self.horizontal = horizontal
        self.title = title
        self.expansion = expansion

    def to_json(self) -> JSONDict:
        return {
            "type": self.type,
            "title": self.title,
            "children": [opt.to_json() for opt in self.options or []],
            "gridSize": self.size,
            "horizontalMode": self.horizontal,
            "expansion": self.expansion.value,
        }
