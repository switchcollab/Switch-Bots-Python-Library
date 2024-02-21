from swibots.utils.types import JSONDict
from .types import Component, Icon, Text
from typing import Union


class FAB(Component):
    type = "fab"

    def __init__(
        self,
        icon: Union[Icon, str],
        name: Union[Text, str] = None,
        color: str = None,
        callback_data: str = None,
    ):
        if isinstance(name, str):
            name = Text(name)
        self.name = name
        if isinstance(icon, str):
            self.icon = Icon(icon)
        self.color = color
        self.callback_data = callback_data

    def to_json(self):
        data = {
            "type": self.type,
            "icon": self.icon.to_json(),
            "text": self.name.to_json(),
        }
        if self.color:
            data["colour"] = self.color
        if self.callback_data:
            data["callbackData"] = self.callback_data
        return data
