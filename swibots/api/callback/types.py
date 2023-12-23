from enum import Enum
from swibots.base import SwitchObject

class ScreenType(Enum):
    BOTTOM = "bottom"

class Component(SwitchObject):
    type = None

class Layout(SwitchObject):
    type = None
