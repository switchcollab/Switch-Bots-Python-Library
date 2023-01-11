from typing import TYPE_CHECKING, List, Optional
from switch.base import SwitchObject

from switch.utils.types import JSONDict

if TYPE_CHECKING:
    from .inline_keyboard_button import InlineKeyboardButton


class InlineMarkup(SwitchObject):
    __slots__ = ("_inline_keyboard",)

    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]] = None,
    ):
        self._inline_keyboard = inline_keyboard

    @property
    def inline_keyboard(self) -> List[List["InlineKeyboardButton"]]:
        if self._inline_keyboard is None:
            self._inline_keyboard = []
        return self._inline_keyboard

    def add_row(self, buttons: List["InlineKeyboardButton"]):
        if len(buttons) > 0:
            self.inline_keyboard.append(list(buttons))

    def to_json(self) -> JSONDict:
        if self._inline_keyboard is None:
            return None
        return {
            "inlineKeyboard": [[x.to_json() for x in row] for row in self._inline_keyboard],
        }

    @classmethod
    def from_json(cls, data: JSONDict) -> "InlineMarkup":
        if data is None or data.get("inlineKeyboard") is None:
            return None
        return cls(
            inline_keyboard=[
                [InlineKeyboardButton.from_json(x) for x in row]
                for row in data.get("inlineKeyboard") or []
            ],
        )
