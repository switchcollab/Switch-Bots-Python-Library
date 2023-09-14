import swibots
from typing import TYPE_CHECKING, Generic, TypeVar
from swibots.api.api_client import ApiClient
from swibots.api.chat.models import Message
from .bot import Bot
from swibots.api.common.events import Event

EventType = TypeVar("EventType", bound="Event")


class BotContext(Generic[EventType], ApiClient):
    def __init__(self, app: "swibots.App", event: EventType):
        self.event = event
        self.app = app
        self._user = app._user

        # copy the api client

        self._chat_client = app.chat_service
        self._auth_client = app.auth_service
        self._community_client = app.community_service
        self._bot_client = app.bots_service

        self.add_handler = self.app.add_handler
        self.remove_handler = self.app.remove_handler
        self.handlers = self.app.handlers
        self.update_bot_commands = self.app.update_bot_commands
        self.set_bot_commands = self.app.set_bot_commands
        self.delete_bot_commands = self.app.delete_bot_commands

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
        return await self.bot.prepare_message(
            receiver_id=receiver_id, text=text, **kwargs
        )

    async def prepare_response_message(self, message: Message) -> Message:
        """
        Prepares a message to be sent as a response to the given message.

        Parameters:
            message (:obj:`switch.api.chat.models.Message`): The message to respond to.

        Returns:
            :obj:`switch.api.chat.models.Message`: The prepared message.
        """
        return await self.bot.prepare_response_message(message=message)
