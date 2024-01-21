from typing import TYPE_CHECKING, Optional
from swibots.api.api_client import ApiClient
from swibots.api.auth.models.auth_user import AuthUser
from swibots.api.bot.models import BotInfo, BotCommand
from swibots.api.chat.models import Message

if TYPE_CHECKING:
    from swibots import Client


class Bot(AuthUser, ApiClient):
    def __init__(self, app: Optional["Client"] = None):
        super().__init__(app)
        self._app = app
        self._info: BotInfo = None

        # copy methods
        self.add_handler = app.add_handler
        self.remove_handler = app.remove_handler
        self.handlers = app.handlers
        self.update_bot_commands = self.app.update_bot_commands
        self.set_bot_commands = self.app.set_bot_commands
        self.delete_bot_commands = self.app.delete_bot_commands

    @property
    def app(self) -> "Client":
        return self._app

    @app.setter
    def app(self, value: "Client"):
        self._app = value
        # copy the api client
        self._chat_client = value.chat_service
        self._auth_client = value.auth_service
        self._community_client = value.community_service
        self._bot_client = value.bots_service

    @property
    def info(self) -> BotInfo:
        """Get the bot info"""
        return self._info

    @info.setter
    def info(self, value: BotInfo):
        """Set the bot info"""
        self._info = value

    @property
    def commands(self) -> list[BotCommand]:
        """Get the bot commands"""
        return self._info.commands or []