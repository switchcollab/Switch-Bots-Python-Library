from typing import TYPE_CHECKING, List, Optional

from swibots.base import SwitchObject
from swibots.utils.types import JSONDict

from .inline_keyboard_button import InlineKeyboardButton
from .inline_keyboard_color import InlineKeyboardColor
from .inline_keyboard_size import InlineKeyboardSize

if TYPE_CHECKING:
    from .inline_keyboard_button import InlineKeyboardButton


class InlineMarkup(SwitchObject):
    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]] = None,
        color: Optional[InlineKeyboardColor] = InlineKeyboardColor.RANDOM,
        size: Optional[InlineKeyboardSize] = InlineKeyboardSize.DEFAULT,
    ):
        super().__init__()
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

    def to_json(self) -> JSONDict | None:
        if self._inline_keyboard is None:
            return None
        return {
            "inlineKeyboard": [[x.to_json() for x in row] for row in self._inline_keyboard],
            "color": self._color.value,
            "size": self._size.value,
        }

    def to_form_data(self):
        form_data = {}
        if self._size is not None:
            form_data["inlineKeyboard.size"] = self._size.value
        if self._color is not None:
            form_data["inlineKeyboard.color"] = self._color.value
        for i, kb in enumerate(self._inline_keyboard):
            for j, b in enumerate(kb):
                text_key = 'inlineKeyboard.inlineKeyboard[{0}][{1}].text'\
                    .format(i, j)
                form_data[text_key] = b.text
                url_key = 'inlineKeyboard.inlineKeyboard[{0}][{1}].url'\
                    .format(i, j)
                form_data[url_key] = b.url
                callback_data_key = 'inlineKeyboard.inlineKeyboard[{0}][{1}].callbackData'\
                    .format(i, j)
                form_data[callback_data_key] = b.callback_data
        return form_data

    def from_json(self, data: JSONDict) -> "InlineMarkup":
        if data is not None and data.get("inlineKeyboard") is not None:
            self._color = InlineKeyboardColor(data.get("color") or "RANDOM")
            self._size = InlineKeyboardSize(data.get("size") or "DEFAULT")
            self._inline_keyboard = [[InlineKeyboardButton.build_from_json(x, self.app) for x in row]
                                     for row in data.get("inlineKeyboard") or []]
        return self
