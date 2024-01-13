from swibots.utils.types import JSONDict
from .types import SwitchObject, Component, Layout
from typing import List, Optional


class ListItem(Layout):
    type = "list_tile"

    def __init__(
        self,
        title: str = None,
        subtitle: str = None,
        callback_data: str = None,
    ):
        self.title = title
        self.subtitle = subtitle
        self.callback_data = callback_data

    def to_json(self) -> JSONDict:
        data = {"type": self.type}
        if self.title:
            data["title"] = self.title
        if self.subtitle:
            data["subTitle"] = self.subtitle
        if self.callback_data:
            data["callbackData"] = self.callback_data
        return data
