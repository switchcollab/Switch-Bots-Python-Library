from typing import Union, List

from swibots.utils.types import JSONDict
from .types import Image, Component, Icon, Text
from enum import Enum


class CardSize(Enum):
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


class CardStyle(Enum):
    TINT = "tint"
    SHADOW = "shadow"
    OUTLINE = "outline"


class Card(Component):
    type = "card"

    def __init__(
        self,
        size: CardSize = CardSize.MEDIUM,
        title: str = "",
        cardType: str = "",
        subtitle: str = "",
        subtitle2: str = "",
        subtitle3: str = "",
        subtitle4: str = "",
        subtitle5: str = "",
        subtitle6: str = "",
        subtitle7: str = "",
        subtitle8: str = "",
        icon: Icon = "",
        icon2: Icon = "",
        icon3: Icon = "",
        icon4: Icon = "",
        icon5: Icon = "",
        callback_data: str = ""
        #        iconAlignment: str = "",
    ):
        self.title = title
        self.cardType = cardType
        self.subTitle = subtitle
        self.subTitle2 = subtitle2
        self.subTitle3 = subtitle3
        self.subTitle4 = subtitle4
        self.subTitle5 = subtitle5
        self.subTitle6 = subtitle6
        self.subTitle7 = subtitle7
        self.subTitle8 = subtitle8
        #        self.image = image
        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        if isinstance(icon2, str):
            icon2 = Icon(icon2)
        self.icon2 = icon2
        if isinstance(icon3, str):
            icon3 = Icon(icon3)
        self.icon3 = icon3
        if isinstance(icon4, str):
            icon4 = Icon(icon4)
        self.icon4 = icon4
        if isinstance(icon5, str):
            icon5 = Icon(icon5)
        self.icon5 = icon5
        self.callback_data = callback_data

    #        self.iconAlignment = iconAlignment
    #        self.size = size

    def to_json(self):
        return {
            "type": self.type,
            "title": self.title,
            "cardType": self.cardType,
            "subTitle": self.subTitle,
            "subTitle2": self.subTitle2,
            "subTitle3": self.subTitle3,
            "subTitle4": self.subTitle4,
            "subTitle5": self.subTitle5,
            "subTitle6": self.subTitle6,
            "subTitle7": self.subTitle7,
            "subTitle8": self.subTitle8,
            #            "image": self.image.to_json() if self.image else None,
            "icon": self.icon.to_json() if self.icon else None,
            "icon2": self.icon2.to_json() if self.icon2 else None,
            "icon3": self.icon3.to_json() if self.icon3 else None,
            "icon4": self.icon4.to_json() if self.icon4 else None,
            "icon5": self.icon5.to_json() if self.icon5 else None,
            "callbackData": self.callback_data
            #            "size": self.size.value,
        }


class CardView(Component):
    type = "card_view"

    def __init__(
        self,
        cards: List[Card],
        card_size: CardSize = CardSize.MEDIUM,
        card_style: CardStyle = CardStyle.TINT,
        vertical_size: CardSize = CardSize.MEDIUM,
        scrollable: bool = False,
        horizontal: bool = False
    ):
        self.card_size = card_size
        self.card_style = card_style
        self.vertical_size = vertical_size
        self.scrollable = scrollable
        self.cards = cards
        self.horizontal = horizontal

    def to_json(self):
        return {
            "type": self.type,
            "cardSize": self.card_size.value,
            "cardStyle": self.card_style.value,
            "verticalSize": self.vertical_size.value,
            "scrollable": self.scrollable,
            "horizontal": self.horizontal,
            "children": [child.to_json() for child in self.cards],
        }


class Banner(Component):
    type = "banner"

    def __init__(
        self,
        title: Union[str, Text],
        heading: Union[str, Text] = "",
        subtitle: Union[str, Text] = "",
        icon: Union[Icon, str] = "",
        background: str = "",
        max_size: bool = False
    ):
        if isinstance(title, str):
            title = Text(title)
        self.title = title

        if isinstance(heading, str):
            heading = Text(heading)
        self.heading = heading

        if isinstance(subtitle, str):
            subtitle = Text(subtitle)
        self.subtitle = subtitle

        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        self.background = background
        self.max_size = max_size

    def to_json(self):
        return {
            "type": self.type,
            "icon": self.icon.to_json() if self.icon else None,
            "heading": self.heading.to_json() if self.heading else None,
            "title": self.title.to_json() if self.title else None,
            "subtitle": self.subtitle.to_json() if self.subtitle else None,
            "background": self.background,
            "mainAxisSize": "max" if self.max_size else "min"
        }
