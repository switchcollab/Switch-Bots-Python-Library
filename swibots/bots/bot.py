from typing import TYPE_CHECKING, Optional
from swibots.api.api_client import ApiClient
from swibots.api.auth.models.auth_user import AuthUser
from swibots.api.bot.models import BotInfo, BotCommand
from swibots.api.chat.models import Message

if TYPE_CHECKING:
    from swibots import BotApp


class Bot(AuthUser, ApiClient):
    def __init__(self, app: Optional["BotApp"] = None):
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
    def app(self) -> "BotApp":
        return self._app

    @app.setter
    def app(self, value: "BotApp"):
        self._app = value
        # copy the api client
        self._chat_client = value.chat_service
        self._auth_client = value.auth_service
        self._community_client = value.community_service
        self._bot_client = value.bots_service

    async def on_app_start(self, app: "BotApp"):
        if app.auto_update_bot:
            """Called when app start
            This method registers the bot commands and updates the bot info
            """
            # await self.update_bot_commands()

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
        message = Message(receiver_id=receiver_id, message=text, app=self.app, **kwargs)
        message.user_id = self.id
        return message

    async def prepare_response_message(self, message: Message) -> Message:
        """
        Prepares a message to be sent as a response to the given message.

        Parameters:
            message (:obj:`switch.api.chat.models.Message`): The message to respond to.

        Returns:
            :obj:`switch.api.chat.models.Message`: The prepared message.
        """
        return message._prepare_response()
