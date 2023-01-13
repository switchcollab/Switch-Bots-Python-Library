import re
from switch.api.chat.models import Message
from switch.bots.constants import EventType, COMMAND_PARSER_REGEX
from switch.bots.events.message_event import MessageEvent


class CommandEvent(MessageEvent):
    """Event for when a message is received from a user."""

    def __init__(self, message: Message):
        super().__init__(message=message)
        self._type = EventType.CHAT_COMMAND
        self._command: str = None
        self._args: str = None
        self.parse_message()

    @property
    def command(self) -> str:
        return self._command

    @property
    def args(self) -> str:
        return self._args

    def parse_message(self):
        self._command, self._args = re.match(COMMAND_PARSER_REGEX, self._message.message).groups()
        self._command = self._command.lower()

    def __str__(self):
        return "Command"
