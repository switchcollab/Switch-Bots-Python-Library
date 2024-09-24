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
        dark_icon: str = "",
        dark_selection_icon: str = "",
        callback_data: str = "",
        selected: bool = False,
    ):
        self.name = name
        self.icon = icon
        self.selected_icon = selection_icon
        self.dark_icon = dark_icon or icon
        self.dark_selection_icon = dark_selection_icon or selection_icon
        self.selected = selected
        self.callback_data = callback_data

    def to_json(self):
        return {
            "name": self.name,
            "icon": self.icon,
            "selectionIcon": self.selected_icon,
            "selected": self.selected,
            "callbackData": self.callback_data,
            "darkIcon": self.dark_icon,
            "darkSelectedIcon": self.dark_selection_icon,
        }


class BottomBarType(Enum):
    DEFAULT = "default"
    TOPLINE = "topline"
    BOTTOMLINE = "bottomline"
    TOP_NOTCH = "top_notch"
    BOTTOM_NOTCH = "bottom_notch"


class BottomBar(SwitchObject):
    def __init__(
        self,
        options: List[BottomBarTile] = None,
        type: BottomBarType = BottomBarType.DEFAULT,
        theme_color: str = "",
    ):
        self.options = options
        self.type = type
        self.theme_color = theme_color

    def from_json(self, data) -> Any:
        if "BottomBar" in data:
            self.type = BottomBarType(data.get("bottomBarStyle"))
            self.options = [
                BottomBarTile().from_json(option) for option in data.get("bottomBar")
            ]
            self.theme_color = data.get("bottomBarColour")

        return self

    def to_json(self):
        data = {
            "bottomBar": [option.to_json() for option in self.options or []],
            "bottomBarStyle": self.type.value,
        }
        if self.theme_color:
            data["bottomBarColour"] = self.theme_color
        return data
