from typing import Union, List

from swibots.utils.types import JSONDict
from .types import Component, Icon


class Accordian(Component):
    def __init__(
        self,
        title: str,
        icon: Union[Icon, str] = "",
        components: List[Component] = None,
    ):
        self.title = title
        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        self.components = components

    def to_json(self):
        data = {
            "title": self.title,
            "icon": self.icon.to_json() if self.icon else None,
        }
        if self.components:
            data["components"] = (
                [component.to_json() for component in self.components],
            )
        return data
