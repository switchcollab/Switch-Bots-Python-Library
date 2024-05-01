from swibots.utils.types import JSONDict
from typing import Dict, Any, Optional, Union
from .types import Component, Icon


class SearchHolder(Component):
    type = "search_holder"

    def __init__(
        self, placeholder: str = "Search..", callback_data: Optional[str] = None,
        max_size: bool = None
    ):
        self.placeholder = placeholder
        self.callback_data = callback_data
        self.max_size = max_size

    def to_json(self) -> Dict[str, Any]:
        data = {
            "type": self.type,
            "placeholder": self.placeholder,
            "mainAxisSize": "max" if self.max_size else "min"
        }
        if self.callback_data:
            data["callbackData"] = self.callback_data
        return data


class SearchBar(Component):
    type = "searchbar"

    def __init__(
        self,
        placeholder: str = "Search",
        value: Optional[str] = None,
        label: Optional[str] = None,
        callback_data: Optional[str] = None,
        right_icon: Union[Icon, str] = Icon(
            "https://img.icons8.com/?size=50&id=KPmthqkeTgDN&format=png"
        ),
        left_icon: Union[Icon, str] = Icon(
            "https://img.icons8.com/?size=50&id=357&format=png",
            "https://img.icons8.com/?size=50&id=357&format=png&color=ffffff",
        ),
    ):
        self.placeholder = placeholder
        self.label = label
        self.value = value

        if isinstance(right_icon, str):
            right_icon = Icon(right_icon)
        self.right_icon = right_icon

        if isinstance(left_icon, str):
            left_icon = Icon(left_icon)
        self.left_icon = left_icon
        self.callback_data = callback_data

    def to_json(self) -> Dict[str, Any]:
        data = {"type": self.type, "placeholder": self.placeholder}
        if self.label:
            data["label"] = self.label
        if self.value:
            data["value"] = self.value
        if self.right_icon:
            data["rightIcon"] = self.right_icon.to_json()
        if self.left_icon:
            data["leftIcon"] = self.left_icon.to_json()
        if self.callback_data:
            data["callbackData"] = self.callback_data
        return data
