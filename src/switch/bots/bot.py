from typing import TYPE_CHECKING
from switch.api.auth.models.auth_user import AuthUser
from switch.api.chat.models import Message

if TYPE_CHECKING:
    from switch import SwitchApp


class Bot(AuthUser):
    def __init__(self):
        super().__init__()
        self._me = None
        self._info = None
        self._app: "SwitchApp" = None

    @property
    def app(self) -> "SwitchApp":
        return self._app

    @app.setter
    def app(self, value: "SwitchApp"):
        self._app = value

    async def on_app_start(self, app: "SwitchApp"):
        """Called when app start
        This method registers the bot commands and updates the bot info
        """
        # get all app commands

        pass

    async def get_me(self) -> dict:
        """Get user bot info"""
        raise NotImplementedError

    async def get_info(self) -> dict:
        """Get bot info"""
        raise NotImplementedError

    async def get_commands(self) -> list:
        """Get the commands"""
        raise NotImplementedError

    async def get_updates(self, **kwargs) -> list:
        """Get updates"""
        raise NotImplementedError

    async def prepare_message(self, receiver_id: int, text: str, **kwargs) -> Message:
        """Prepare a message to be sent to a user"""
        message = Message(receiver_id=receiver_id, message=text, **kwargs)
        message.user_id = self.id
        return message

    async def prepare_response_message(self, message: Message) -> Message:
        """Prepare a message to be sent to a user that is a response to a message"""
        message = Message(receiver_id=message.user_id, message=message.message)
        message.user_id = self.id
        return message

    async def send_message(self, message: Message) -> Message | bool:
        message.user_id = self.id
        return await self.app.api.chat.messages.send_message(message=message)

    async def edit_message(self, message: Message) -> Message | bool:
        message.user_id = self.id
        return await self.app.api.chat.messages.edit_message(message=message)

    async def edit_message_text(self, message: Message, text: str, **kwargs) -> Message | bool:
        message.message = text
        return self.edit_message(message=message)

    async def delete_message(self, message: int | Message, **kwargs) -> bool:
        """Delete a message"""
        return await self.app.api.chat.messages.delete_message(message=message)
