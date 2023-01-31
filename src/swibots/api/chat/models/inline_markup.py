from typing import TYPE_CHECKING, List, Optional
import swibots
from .inline_keyboard_color import InlineKeyboardColor
from .inline_keyboard_size import InlineKeyboardSize
from .inline_keyboard_button import InlineKeyboardButton
from swibots.base import SwitchObject

from swibots.utils.types import JSONDict

if TYPE_CHECKING:
    from .inline_keyboard_button import InlineKeyboardButton


class InlineMarkup(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        inline_keyboard: List[List["InlineKeyboardButton"]] = None,
        color: Optional[InlineKeyboardColor] = InlineKeyboardColor.RANDOM,
        size: Optional[InlineKeyboardSize] = InlineKeyboardSize.DEFAULT,
    ):
        super().__init__(app)
        self._inline_keyboard = inline_keyboard
        self._color = color or InlineKeyboardColor.RANDOM
        self._size = size or InlineKeyboardSize.DEFAULT

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
            "color": self._color.value,
            "size": self._size.value,
        }

    def from_json(self, data: JSONDict) -> "InlineMarkup":
        if data is None or data.get("inlineKeyboard") is None:
            return None
        self._color = InlineKeyboardColor(data.get("color") or "RANDOM")
        self._size = InlineKeyboardSize(data.get("size") or "DEFAULT")
        self._inline_keyboard = (
            [
                [InlineKeyboardButton.build_from_json(
                    x, self.app) for x in row]
                for row in data.get("inlineKeyboard") or []
            ],
        )

        return self
