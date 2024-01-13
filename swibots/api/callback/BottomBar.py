from enum import Enum
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict
from typing import Dict, Any, List


class BottomBarTile(SwitchObject):
    def __init__(
        self,
        name: str,
        icon: str = "",
        selection_icon: str = "",
        callback_data: str = "",
        selected: bool = False,
    ):
        self.name = name
        self.icon = icon
        self.selected_icon = selection_icon
        self.selected = selected
        self.callback_data = callback_data

    def to_json(self):
        return {
            "name": self.name,
            "icon": self.icon,
            "selectedIcon": self.selected_icon,
            "selected": self.selected,
            "callbackData": self.callback_data,
        }


class BottomBarTypes(Enum):
    DEFAULT = "default"
    TOPLINE = "topline"
    BOTTOMLINE = "bottomline"
    TOP_NOTCH = "top_notch"
    BOTTOM_NOTCH = "bottom_notch"


class BottomBar(SwitchObject):
    def __init__(
        self,
        options: List[BottomBarTile],
        type: BottomBarTypes = BottomBarTypes.DEFAULT,
        theme_color: str = "",
    ):
        self.options = options
        self.type = type
        self.theme_color = theme_color

    def to_json(self):
        data = {
            "bottomBar": [option.to_json() for option in self.options],
            "bottomBarStyle": self.type.value,
        }
        if self.theme_color:
            data["bottomBarColour"] = self.theme_color
        return data
