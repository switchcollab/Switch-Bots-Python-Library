from swibots.utils.types import JSONDict
from .types import Component
from enum import Enum
from typing import List
from swibots.base import SwitchObject


class TabBarTile(SwitchObject):
    def __init__(
        self,
        title: str = "",
        callback_data: str = None,
        selected: bool = False,
        selection_icon: str = None,
    ):
        self.title = title
        self.callback_data = callback_data
        self.selected = selected
        self.selection_icon = selection_icon

    def to_json(self):
        return {
            "icon": self.title,
            "selected": self.selected,
            "callbackData": self.callback_data,
            "selectionIcon": self.selection_icon,
        }


class TabBarType(Enum):
    SWIPE = "swipe_tab"
    SEGMENTED = "segmented_tab"
    BUTTON = "button_tab"


class TabBar(Component):
    type = "tab"

    def __init__(
        self,
        tabs: List[TabBarTile],
        bar_type: TabBarType = TabBarType.SWIPE,
    ):
        self.bar_type = bar_type
        self.tabs = tabs

    def to_json(self):
        return {
            "type": self.type,
            "tabs": [tab.to_json() for tab in self.tabs],
            "tabBarStyle": self.bar_type.value,
        }
