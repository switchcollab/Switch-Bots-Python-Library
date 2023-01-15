from typing import TYPE_CHECKING, Generic, TypeVar
from switch.api.chat.models import Message
from .bot import Bot
from switch.api.common.events import Event

if TYPE_CHECKING:
    from switch import SwitchApp


EventType = TypeVar("EventType", bound="Event")


class BotContext(Generic[EventType]):
    def __init__(self, bot: "Bot", event: EventType, app: "SwitchApp"):
        self.event = event
        self.bot = bot
        self.app = app

    async def prepare_message(self, receiver_id: int, text: str, **kwargs) -> Message:
        return self.bot.prepare_message(receiver_id=receiver_id, text=text, **kwargs)

    async def prepare_response_message(self, message: Message) -> Message:
        return self.bot.prepare_response_message(message=message)

    async def send_message(self, message: Message) -> Message | bool:
        return self.bot.send_message(message=message)

    async def edit_message(self, message: Message) -> Message | bool:
        return self.bot.edit_message(message=message)

    async def edit_message_text(self, message: Message, text: str, **kwargs) -> Message | bool:
        return self.bot.edit_message_text(message=message, text=text, **kwargs)

    async def delete_message(self, message: int | Message, **kwargs) -> bool:
        return self.bot.delete_message(message=message, **kwargs)
