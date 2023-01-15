from typing import Optional
from switch.base.switch_object import SwitchObject
from switch.types import EventType
from switch.utils.types import JSONDict


class Event(SwitchObject):
    __slots__ = ("event_type", "data")

    def __init__(
        self,
        type: Optional[EventType] = None,
        data: Optional[dict] = None,
    ):
        self.type = type
        self.data = data

    def from_json(self, data: JSONDict) -> "Event":
        if data is not None:
            details = data.get("details") or {}
            self.type = EventType(data.get("type"))
            self.data = details
        return self

    def to_json(self) -> JSONDict:
        return {
            "type": self.type,
            "details": self.data,
        }
