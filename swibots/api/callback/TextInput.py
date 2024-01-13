from .types import Component, Icon
from typing import Optional

from enum import Enum

class KeyboardType(Enum):
    NUMBER = "number"
    TEXT = "text"
    EMAIL = "email"
    URL = "url"


class TextInput(Component):
    type = "input_box"

    def __init__(
        self,
        label: str,
        value: str = "",
        width: int = 0,
        placeholder: Optional[str] = None,
        callback_data: Optional[str] = None,
        keyboardType: KeyboardType = KeyboardType.DEFAULT,
        error: bool = False,
        error_text: Optional[str] = None,
        password: bool = False,
        right_icon: Optional[Icon] = None,
        left_icon: Optional[Icon] = None,
    ):
        self.label = label
        self.width = width
        self.value = value
        self.placeholder = placeholder
        self.callback_data = callback_data
        self.keyboard_type = keyboardType
        self.error = error
        self.error_text = error_text
        self.password = password

        if isinstance(right_icon, str):
            right_icon = Icon(right_icon)
        self.right_icon = right_icon

        if isinstance(left_icon, str):
            left_icon = Icon(left_icon)
        self.left_icon = left_icon

    def to_json(self):
        data = {
            "type": self.type,
            "label": self.label,
            "width": self.width,
            "value": self.value,
            "placeholder": self.placeholder,
            "callbackData": self.callback_data,
            "keyboardType": self.keyboard_type.value,
            "error": self.error,
            "errorText": self.error_text,
            "password": self.password,
        }
        if self.right_icon:
            data["rightIcon"] = self.right_icon.to_json()
        if self.left_icon:
            data["leftIcon"] = self.left_icon.to_json()
        return data
