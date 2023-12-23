from swibots.base import SwitchObject
from swibots.utils.types import JSONDict
from .types import ScreenType, Layout, Component
from typing import List, Optional, Dict, Any

class AppBar(SwitchObject):
    def __init__(self, title: str = None,
                 subtitle: str = None):
        self.title = title
        self.subtitle = subtitle
    
    def to_json(self) -> JSONDict:
        return {
            "title": self.title,
            "subtitle": self.subtitle
        }


class AppPage(SwitchObject):
    def __init__(
        self,
        screen: ScreenType = ScreenType.BOTTOM,
        layouts: List[Layout] = None,
        components: List[Component] = None,
        app_bar: AppBar = None
    ):
        self.type = "appPage"
        self.screen = screen
        self.layouts = layouts or []
        self.components = components or []
        self.app_bar = app_bar

    def to_json(self) -> JSONDict:
        data = {
            "type": self.type,
            "mode": self.screen.value,
            "layouts": [layout.to_json() for layout in self.layouts],
            "components": [component.to_json() for component in self.components],
        }
        if self.app_bar:
            data['pageBar'] = self.app_bar.to_json()
        return data
