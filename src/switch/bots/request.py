from typing import Optional
from switch.bots.constants import RequestType


class Request:
    def __init__(self, type: RequestType, data: Optional[dict] = None):
        self._type = type
        self._data = data or {}
        self._message = None
        self._callback_query = None

    
    @property
    def type(self) -> RequestType:
        return self._type

    @property
    def message(self):
        return self._message