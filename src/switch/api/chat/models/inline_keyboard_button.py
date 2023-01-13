from typing import List, Optional
from switch.base import SwitchObject

from switch.utils.types import JSONDict


class InlineKeyboardButton(SwitchObject):
    __slots__ = ("text", "url", "callback_data")

    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data

    def to_json(self) -> JSONDict:
        return {
            "text": self.text,
            "url": self.url,
            "callbackData": self.callback_data,
        }

    def from_json(self, data: JSONDict) -> "InlineKeyboardButton":
        if data is not None:
            self.text = (data.get("text"),)
            self.url = (data.get("url"),)
            self.callback_data = (data.get("callbackData"),)
        return self
