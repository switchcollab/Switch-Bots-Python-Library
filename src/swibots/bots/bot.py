from typing import TYPE_CHECKING, Optional
from swibots.api.api_client import ApiClient
from swibots.api.auth.models.auth_user import AuthUser
from swibots.api.bot.models import BotInfo, BotCommandInfo
from swibots.api.chat.models import Message

if TYPE_CHECKING:
    from swibots import BotApp


class Bot(AuthUser, ApiClient):
    def __init__(self, app: Optional["BotApp"] = None):
        super().__init__(app)
        self._info: BotInfo = None

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
            # get all app commands
            commands = self.app._register_commands or []
            description = self.app._bot_description or ""
            # register the commands
            self._info = BotInfo(description=description, id=self.id)
            for command in commands:
                command_name = command.command
                if isinstance(command_name, str):
                    command_names = command_name.split(",")
                else:
                    command_names = command_name

                for c_name in command_names:
                    self.info.commands.append(
                        BotCommandInfo(
                            command=c_name,
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
        message = Message(receiver_id=receiver_id,
                          message=text, app=self.app, **kwargs)
        message.user_id = self.id
        return message

    # async def prepare_response_message(self, message: Message) -> Message:
    #     """
    #     Prepares a message to be sent as a response to the given message.

    #     Parameters:
    #         message (:obj:`switch.api.chat.models.Message`): The message to respond to.

    #     Returns:
    #         :obj:`switch.api.chat.models.Message`: The prepared message.
    #     """

    #     receiver_id = message.user_id if message.user_id != self.id else message.receiver_id
    #     sender_id = self.id
    #     m = Message.build_from_json(message.to_json(), self.app)
    #     m.id = None
    #     m.message = ""

    #     if message.community_id is None or message.community_id == "":
    #         m.receiver_id = receiver_id

    #     m.user_id = sender_id
    #     return m

    async def prepare_response_message(self, message: Message) -> Message:
        """
        Prepares a message to be sent as a response to the given message.

        Parameters:
            message (:obj:`switch.api.chat.models.Message`): The message to respond to.

        Returns:
            :obj:`switch.api.chat.models.Message`: The prepared message.
        """

        response = Message(self.app)

        if message.community_id is not None and message.community_id != "":
            response.community_id = message.community_id
            response.group_id = message.group_id
            response.channel_id = message.channel_id
        else:
            receiver_id = message.user_id if message.user_id != self.id else message.receiver_id
            response.receiver_id = receiver_id

        response.user_id = self.id
        return response
