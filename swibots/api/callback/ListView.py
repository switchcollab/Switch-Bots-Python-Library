from swibots.utils.types import JSONDict
from .types import SwitchObject, Component, Image, Badge
from enum import Enum
from typing import Union, List, Literal


class ListViewType(Enum):
    DEFAULT = "default"
    SMALL = "small"
    LARGE = "large"
    COMPACT = "compact"


class ListTile(Component):
    type = "list_tile"

    def __init__(
        self,
        title: str,
        description: str = "",
        subtitle: str = "",
        title_extra: str = "",
        description_extra: str = "",
        subtitle_extra: str = "",
        callback_data: str = "",
        thumb: Union[Image, str] = "",
        badges: List[Badge] = None,
        max_size: bool = None,
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
        self.badges = badges
        self.max_size = max_size

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
            "mainAxisSize": "max" if self.max_size else "min",
        }
        if self.thumb:
            data["image"] = self.thumb.to_json()
        if self.badges:
            data["rightComponents"] = [badge.to_json() for badge in self.badges]
        return data


class SmallListTile(ListTile):
    def __init__(
        self, title: str, icon: Union[str, Image] = None, callback_data: str = None
    ):
        super().__init__(title=title, callback_data=callback_data, thumb=icon)


class ListView(Component):
    type = "list_view"

    def __init__(
        self,
        options: List[Union[ListTile, SmallListTile]],
        view_type: ListViewType = ListViewType.DEFAULT,
        title: str = None,
        right_image: str = None,
        image_callback: str = None,
        max_size: bool = None,
    ):
        self.title = title
        self.options = options
        self.view_type = view_type
        self.right_image = right_image
        self.image_callback = image_callback
        self.max_size = max_size

    def to_json_request(self):
        if self.view_type == ListViewType.COMPACT:
            return {
                "type": self.type,
                "title": self.title,
                "listStyle": self.view_type.value,
                "subTitle": self.right_image,
                "subTitleAction": self.image_callback,
                "lists": [tile.to_json() for tile in self.options],
                "mainAxisSize": "max" if self.max_size else "min",
            }

        options = []

        for opt in self.options:
            opt = opt.to_json()
            opt["listStyle"] = self.view_type.value
            opt["mainAxisSize"] = "max" if self.max_size else "min"
            options.append(opt)

        return options
