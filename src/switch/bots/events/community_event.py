from switch.bots.constants import EventType
from .event import Event
from switch.api.chat.models import Message


class CommunityEvent(Event):
    def __init__(self, message: Message):
        super().__init__(EventType.CHAT_MESSAGE)
        self._message = message
        self.parse_message()

    def parse_message(self):
        pass

    def __str__(self):
        return "Message"
