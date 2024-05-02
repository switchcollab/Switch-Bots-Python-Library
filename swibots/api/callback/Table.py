from typing import List, Union

from swibots.utils.types import JSONDict
from .types import Text, Icon, Component


class TableTile(Component):
    type = "table_tile"

    def __init__(
        self,
        title: Union[Text, str],
        icon: Union[Icon, str],
        subtitle: str = "",
        callback_data: str = None,
    ):
        if isinstance(title, str):
            title = Text(title)
        self.title = title

        if isinstance(icon, str):
            icon = Icon(icon)
        self.icon = icon
        self.subtitle = subtitle
        self.callback_data = callback_data

    def to_json(self):
        return {
            "title": self.title.to_json(),
            "icon": self.icon.to_json(),
            "subTitle": self.subtitle,
            "callbackData": self.callback_data,
            "type": self.type,
        }


class Table(Component):
    type = "table"

    def __init__(
        self,
        headings: List[TableTile],
        rows: List[List[TableTile]],
        title: str = "",
        scoreboard: bool = False,
        max_size: bool = None,
    ):
        self.title = title
        self.headings = headings
        self.rows = rows
        self.columns_count = len(headings)
        self.scoreboard = scoreboard
        self.max_size = max_size

    def to_json(self):
        return {
            "type": self.type,
            "headings": [heading.to_json() for heading in self.headings],
            "rows": [[row.to_json() for row in col] for col in self.rows],
            "columnsCount": self.columns_count,
            "version": 1 if self.scoreboard else 0,
            "mainAxisSize": "max" if self.max_size else "min",
        }
