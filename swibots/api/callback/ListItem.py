from swibots.utils.types import JSONDict
from .types import SwitchObject, Component, Layout
from typing import List, Optional

class ListItem(Layout):
    type = "list_tile"

    def __init__(self, title: str = None,
                 subtitle: str = None,
                 subtitle2: str = None,
                 subtitle_action: str = None,
                 callback_data: str = None,
                 right: List[Component] = None,
                 left: List[Component] = None
                 ):
        self.title = title
        self.subtitle = subtitle
        self.subtitle2 = subtitle2
        self.subtitle_action = subtitle_action
        self.callback_data = callback_data
        self.right = right
        self.left = left
    
    def to_json(self) -> JSONDict:
        data = {"type": self.type}
        if self.title:
            data['title'] = self.title
        if self.subtitle:
            data['subTitle'] = self.subtitle
        if self.subtitle2:
            data['subTitle2'] = self.subtitle2
        if self.subtitle_action:
            data['subTitleAction'] = self.subtitle_action
        if self.callback_data:
            data['callbackData'] = self.callback_data
        return data