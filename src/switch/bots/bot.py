from typing import TYPE_CHECKING
from switch.api.api_client import ApiClient
from switch.api.auth.models.auth_user import AuthUser
from switch.api.bot.models import BotInfo, BotCommandInfo
from switch.api.chat.models import Message

if TYPE_CHECKING:
    from switch import BotApp


class Bot(AuthUser, ApiClient):
    def __init__(self):
        super().__init__()
        self._info: BotInfo = None
        self._app: "BotApp" = None

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
        """Called when app start
        This method registers the bot commands and updates the bot info
        """
        # get all app commands
        commands = self.app._register_commands or []
        description = self.app._description or ""
        # register the commands
        self._info = BotInfo(description=description, id=self.id)
        for command in commands:
            self.info.commands.append(
                BotCommandInfo(
                    command=command.command,
                    description=command.description,
                    channel=command.channel,
                )
            )
        self.info = await self.update_bot_info(self.info)

        pass

    @property
    def info(self) -> BotInfo:
        """Get the bot info"""
        return self._info

    @info.setter
    def info(self, value: BotInfo):
        """Set the bot info"""
        self._info = value

    @property
    def commands(self) -> list[BotCommandInfo]:
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
        message = Message(receiver_id=receiver_id, message=text, **kwargs)
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
        message = Message(receiver_id=message.user_id, message=message.message)
        message.user_id = self.id
        return message
