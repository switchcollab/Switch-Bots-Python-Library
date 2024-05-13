from typing import Optional, List, Union

from enum import Enum
from swibots.utils.types import JSONDict
from .types import Component, Text, Icon


class ButtonVariant(Enum):
    ROUNDED = "rounded"
    OUTLINED = "outlined"
    DEFAULT = "elevated"


class Button(Component):
    type = "action_button"

    def __init__(
        self,
        text: Union[str, Text],
        icon: Union[str, Icon] = "",
        callback_data: Optional[str] = None,
        color: str = None,
        variant: ButtonVariant = ButtonVariant.DEFAULT,
        max_size: bool = None,
        **kwargs
    ):
        if isinstance(text, str):
            text = Text(text)
        self.text = text
        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        self.callback_data = callback_data
        self.color = color
        self.variant = variant
        self.clipboard = kwargs.get("clipboard")
        self.action = kwargs.get("action")
        self.url = kwargs.get("url")
        self.file_name = kwargs.get("downloadFileName")
        self.max_size = max_size

    def to_json(self):
        data = {
            "type": self.type,
            "text": self.text.to_json() if self.text else None,
            "callbackData": self.callback_data if self.callback_data else None,
            "color": self.color,
            "variant": self.variant.value,
            "mainAxisSize": "max" if self.max_size else "min",
        }
        if self.icon:
            data["icon"] = self.icon.to_json()
        if self.url:
            data["url"] = self.url
        if self.action:
            data["action"] = self.action
        if self.file_name:
            data["downloadFileName"] = self.file_name
        if self.clipboard:
            data["clipboard"] = True
        return data


class AdButton(Button):
    """
    AdButton: Show Button with different animation for ads.
    """

    def __init__(self, text: Union[str, Text], callback_data: str, **kwargs):
        super().__init__(
            text=text, action="show_ad", callback_data=callback_data, **kwargs
        )


class DownloadButton(Button):
    def __init__(
        self,
        download_url: str,
        file_name: str,
        text: str | Text = "Download",
        icon: str | Icon = "",
        callback_data: str = None,
    ):
        super().__init__(
            text,
            icon,
            url=download_url,
            file_name=file_name,
            action="download",
            callback_data=callback_data,
        )


class ShareButton(Button):
    def __init__(
        self,
        text: str | Text,
        icon: str | Icon = "",
        share_text: str = "",
        color: str = None,
        variant: ButtonVariant = ButtonVariant.DEFAULT,
        **kwargs
    ):
        super().__init__(text, icon, color=color, variant=variant, **kwargs)
        self.share_text = share_text

    def to_json(self):
        data = super().to_json()
        data.update({"share": True, "shareText": self.share_text})
        return data


class ClipboardButton(Button):
    def __init__(
        self, text: str | Text, icon: str | Icon = "", url: str = "", **kwargs
    ):
        super().__init__(text, icon, clipboard=True, url=url, **kwargs)


class ButtonGroup(Component):
    type = "button_group"

    def __init__(self, buttons: List[Button], max_size: bool = None, flexible=False):
        self.buttons = buttons
        self.max_size = max_size
        self.flexible = flexible

    def to_json(self):
        return {
            "type": self.type,
            "buttons": [button.to_json() for button in self.buttons],
            "mainAxisSize": "max" if self.max_size else "min",
            "flexible": self.flexible
        }


class StickyHeader(Component):
    type = "sticky_header"

    def __init__(
        self,
        text: str,
        color: str = None,
        callback_data: str = None,
        icon: Icon = None,
    ):
        self.text = text
        self.color = color
        self.callback_data = callback_data
        self.icon = icon

    def to_json(self):
        return {
            "type": self.type,
            "text": self.text,
            "color": self.color,
            "callbackData": self.callback_data,
            "icon": self.icon.to_json() if self.icon else None,
        }
