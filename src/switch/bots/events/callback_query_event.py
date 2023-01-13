import re

import switch

from switch.api.chat.models import Message
from switch.bots.constants import EventType

from ..events.message_event import MessageEvent


class CallbackQueryEvent(MessageEvent):
    """Event for when a message is received from a user."""

    def __init__(self, message: Message):
        super().__init__(message=message)
        self._type = EventType.CHAT_CALLBACK_QUERY
        self._callback_data: str = None
        self.parse_message()

    @property
    def callback_data(self) -> str:
        return self._callback_data

    def parse_message(self):
        if self._message.callback_data is not None:
            self._callback_data = self._message.callback_data

    def __str__(self):
        return "Command"
