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

    @classmethod
    def from_json(cls, data: JSONDict) -> "InlineKeyboardButton":
        return cls(
            text=data.get("text"),
            url=data.get("url"),
            callback_data=data.get("callbackData"),
        )
