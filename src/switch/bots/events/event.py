from typing import Optional
from switch.api.chat.models import Message
from switch.bots.constants import EventType


class Event:
    def __init__(self, type: EventType, data: Optional[dict] = None):
        self._type = type
        self._data = data or {}

    @property
    def type(self) -> EventType:
        return self._type

    @property
    def message(self) -> Optional["Message"]:
        return self._message
