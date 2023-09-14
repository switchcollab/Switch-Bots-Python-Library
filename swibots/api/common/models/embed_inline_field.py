from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject


class EmbedInlineField(SwitchObject):
    def __init__(
        self,
        icon: Optional[str] = None,
        key: Optional[str] = None,
        title: Optional[str] = None,
    ):
        super().__init__()
        self.icon = icon
        self.key = key
        self.title = title

    def to_json(self) -> JSONDict:
        return {"icon": self.icon, "key": self.key, "title": self.title}
