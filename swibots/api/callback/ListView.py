from swibots.utils.types import JSONDict
from .types import SwitchObject, Layout, Image
from enum import Enum
from typing import Union, List, Literal


class ListViewType(Enum):
    DEFAULT = "default"
    SMALL = "small"
    LARGE = "large"


class ListTile(Layout):
    type = "list_tile"

    def __init__(
        self,
        title: str,
        description: str = "",
        subtitle: str ="",
        title_extra: str = "",
        description_extra: str = "",
        subtitle_extra: str = "",
        callback_data: str = "",
        thumb: Union[Image, str] = "",
    ):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.title_extra = title_extra
        self.description_extra = description_extra
        self.subtitle_extra = subtitle_extra
        self.callback_data = callback_data
        if isinstance(thumb, str):
            thumb = Image(thumb)
        self.thumb = thumb

    def to_json(self):
        data = {
            "type": self.type,
            "title": self.title,
            "subTitle1": self.title_extra,
            "subTitle2": self.description,
            "subtitle3": self.description_extra,
            "subtitle4": self.subtitle,
            "subTitle5": self.subtitle_extra,
            "callbackData": self.callback_data,
        }
        if self.thumb:
            data["image"] = self.thumb.to_json()
        return data


class SmallListTile(ListTile):
    def __init__(
        self, title: str, icon: Union[str, Image] = None, callback_data: str = None
    ):
        super().__init__(title=title, callback_data=callback_data, thumb=icon)


class ListView(Layout):
    def __init__(
        self,
        options: List[Union[ListTile, SmallListTile]],
        view_type: ListViewType = ListViewType.DEFAULT,
    ):
        self.options = options
        self.view_type = view_type

    def to_json_request(self):
        options = []

        for opt in self.options:
            opt = opt.to_json()
            opt["listStyle"] = self.view_type.value
            options.append(opt)

        return options
