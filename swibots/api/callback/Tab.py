from swibots.utils.types import JSONDict
from .types import Layout
from enum import Enum
from typing import List
from swibots.base import SwitchObject


class TabBarTile(SwitchObject):
    def __init__(
        self, title: str = "", callback_data: str = None, selected: bool = False
    ):
        self.title = title
        self.callback_data = callback_data
        self.selected = selected

    def to_json(self):
        return {
            "icon": self.title,
            "selected": self.selected,
            "callbackData": self.callback_data,
        }


class TabBarType(Enum):
    SWIPE = "swipe_tab"
    SEGMENTED = "segmented_tab"
    BUTTON = "button_tab"


class TabBar(Layout):
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
            "tabs": [tab.to_json() for tab in self.tabs],
            "tabBarStyle": self.bar_type,
        }
