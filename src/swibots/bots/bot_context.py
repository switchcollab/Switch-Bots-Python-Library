from typing import TYPE_CHECKING, Generic, TypeVar
from swibots.api.api_client import ApiClient
from swibots.api.chat.models import Message
from .bot import Bot
from swibots.api.common.events import Event

EventType = TypeVar("EventType", bound="Event")


class BotContext(Generic[EventType], ApiClient):
    def __init__(self, bot: "Bot", event: EventType):
        self.event = event
        self.bot = bot
        # copy the api client
        self._chat_client = bot.chat_service
        self._auth_client = bot.auth_service
        self._community_client = bot.community_service
        self._bot_client = bot.bots_service

    async def prepare_message(self, receiver_id: int, text: str, **kwargs) -> Message:
        """
        Prepares a message to be sent to the given receiver.

        Parameters:
            receiver_id (:obj:`int`): The receiver's id.
            text (:obj:`str`): The message's text.
            **kwargs: Additional keyword arguments to pass to the message constructor.

        Returns:
            :obj:`switch.api.chat.models.Message`: The prepared message.
        """
        return await self.bot.prepare_message(receiver_id=receiver_id, text=text, **kwargs)

    async def prepare_response_message(self, message: Message) -> Message:
        """
        Prepares a message to be sent as a response to the given message.

        Parameters:
            message (:obj:`switch.api.chat.models.Message`): The message to respond to.

        Returns:
            :obj:`switch.api.chat.models.Message`: The prepared message.
        """
        return await self.bot.prepare_response_message(message=message)
