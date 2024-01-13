from typing import Optional, List, Union

from swibots.utils.types import JSONDict
from .types import Component, Text, Icon


class Button(Component):
    type = "action_button"

    def __init__(
        self,
        text: Union[str, Text],
        icon: Union[str, Icon] = "",
        callback_data: Optional[str] = None,
        **kwargs
    ):
        if isinstance(text, str):
            text = Text(text)
        self.text = text
        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        self.callback_data = callback_data
        self.action = kwargs.get("action")
        self.url = kwargs.get("url")
        self.file_name = kwargs.get("downloadFileName")

    def to_json(self):
        data = {
            "type": self.type,
            "text": self.text.to_json() if self.text else None,
            "callbackData": self.callback_data if self.callback_data else None,
        }
        if self.icon:
            data["icon"] = self.icon.to_json()
        if self.url:
            data["url"] = self.url
        if self.action:
            data["action"] = self.action
        if self.file_name:
            data["downloadFileName"] = self.file_name
        return data


class DownloadButton(Button):
    def __init__(
        self,
        download_url: str,
        file_name: str,
        text: str | Text = "Download",
        icon: str | Icon = "",
        callback_data: str = None
    ):
        super().__init__(
            text, icon, url=download_url, file_name=file_name, action="download",
            callback_data=callback_data
        )


# TODO:
class ShareButton(Button):
    ...


class ButtonGroup(Component):
    type = "button_group"

    def __init__(self, buttons: List[Button]):
        self.buttons = buttons

    def to_json(self):
        return {
            "type": self.type,
            "buttons": [button.to_json() for button in self.buttons],
        }
