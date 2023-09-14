from typing import TYPE_CHECKING, List, Optional
import swibots

from swibots.base import SwitchObject
from swibots.utils.types import JSONDict

from .inline_keyboard_button import InlineKeyboardButton

if TYPE_CHECKING:
    from .inline_keyboard_button import InlineKeyboardButton


class InlineMarkup(SwitchObject):
    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]] = None,
    ):
        super().__init__()
        self._inline_keyboard = inline_keyboard

    @property
    def inline_keyboard(self) -> List[List["InlineKeyboardButton"]]:
        if self._inline_keyboard is None:
            self._inline_keyboard = []
        return self._inline_keyboard

    def add_row(self, buttons: List["InlineKeyboardButton"]):
        if len(buttons) > 0:
            self.inline_keyboard.append(list(buttons))

    def to_json(self) -> JSONDict | None:
        if self._inline_keyboard is None:
            return None
        return {
            "inlineKeyboard": [
                [x.to_json() for x in row] for row in self._inline_keyboard
            ],
        }

    def to_form_data(self):
        form_data = {}
        for i, kb in enumerate(self._inline_keyboard):
            for j, b in enumerate(kb):
                text_key = "inlineKeyboard.inlineKeyboard[{0}][{1}].text".format(i, j)
                form_data[text_key] = b.text
                url_key = "inlineKeyboard.inlineKeyboard[{0}][{1}].url".format(i, j)
                form_data[url_key] = b.url
                game_key = "inlineKeyboard.inlineKeyboard[{0}][{1}].game".format(i, j)
                form_data[game_key] = b.game
                callback_data_key = (
                    "inlineKeyboard.inlineKeyboard[{0}][{1}].callbackData".format(i, j)
                )
                form_data[callback_data_key] = b.callback_data

        return form_data

    def from_json(self, data: JSONDict) -> "InlineMarkup":
        if data is not None and data.get("inlineKeyboard") is not None:
            self._inline_keyboard = [
                [InlineKeyboardButton.build_from_json(x, self.app) for x in row]
                for row in data.get("inlineKeyboard") or []
            ]
        return self


class InlineMarkupRemove(InlineMarkup):
    """InlineMarkupRemove: InlineMarkup class to remove inline buttons"""

    def __init__(self):
        ...
