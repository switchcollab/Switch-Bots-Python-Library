import swibots
from swibots.base import SwitchObject
from logging import getLogger
from swibots.utils.types import JSONDict
from .types import ScreenType, Layout, Component, Icon
from typing import List, Optional, Dict, Any, Union

LOG = getLogger(__name__)


class AppBar(SwitchObject):
    def __init__(
        self,
        title: str = "App",
        subtitle: str = "",
        left_icon: Union[Icon, str] = Icon(
            "https://raw.githubusercontent.com/switchcollab/Switch-Bots-Python-Library/main/docs/static/img/logo.png"
        ),
        secondary_icon: Union[Icon, str] = None,
        tertiary_icon: Union[Icon, str] = ""
    ):
        self.title = title
        self.subtitle = subtitle

        if isinstance(left_icon, str):
            left_icon = Icon(left_icon)
        self.left_icon = left_icon

        if isinstance(secondary_icon, str):
            secondary_icon = Icon(secondary_icon)
        self.secondary_icon = secondary_icon

        if isinstance(tertiary_icon, str):
            tertiary_icon = Icon(tertiary_icon)
        self.tertiary_icon = tertiary_icon

    def to_json(self) -> JSONDict:
        data = {"title": self.title, "subtitle": self.subtitle}
        if self.left_icon:
            data["leftIcon"] = self.left_icon.to_json()
        if self.secondary_icon:
            data["secondaryIcon"] = self.secondary_icon.to_json()
        if self.tertiary_icon:
            data["tertiaryIcon"] = self.tertiary_icon.to_json()
        return data


class AppPage(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        screen: ScreenType = ScreenType.SCREEN,
        layouts: List[Layout] = None,
        components: List[Component] = None,
        app_bar: AppBar = None,
    ):
        super().__init__(app)
        self.type = "appPage"
        self.screen = screen
        self.layouts = layouts or []
        self.components = components or []
        self.app_bar = app_bar

    def to_json(self) -> JSONDict:
        layouts = []
        components = []
        for layout in self.layouts:
            if isinstance(layout, Layout):
                layouts.append(layout.to_json())
            else:
                LOG.warning(f"Ignoring: {layout}: type is not layout.")
        for component in self.components:
            if isinstance(component, Component):
                components.append(component.to_json())
            else:
                LOG.warning(f"Ignoring: {layout}: type is not component.")

        data = {
            "type": self.type,
            "mode": self.screen.value,
            "layouts": layouts,
            "components": components,
        }
        if self.app_bar:
            data["pageBar"] = self.app_bar.to_json()
        return data
