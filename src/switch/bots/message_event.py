from switch.bots.constants import EventType
from .event import Event
from switch.api.chat.models import Message


class MessageEvent(Event):
    """Event for when a message is received from a user."""

    def __init__(self, message: Message):
        super().__init__(EventType.MESSAGE)
        self._message = message
        self.parse_message()

    def parse_message(self):
        pass

    def __str__(self):
        return "Message"