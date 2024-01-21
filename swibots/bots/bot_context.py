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