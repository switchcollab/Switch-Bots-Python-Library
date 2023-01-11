import json
import logging
from typing import TYPE_CHECKING, List
from switch.api.chat.models import Message
from switch.error import SwitchError
from switch.utils.types import JSONDict

if TYPE_CHECKING:
    from switch.api.chat import ChatClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/message/v1"


class MessageController:
    def __init__(self, client: "ChatClient"):
        self.client = client

    async def get_messages(self, user_id: int = None) -> List[Message]:
        if user_id is None:
            user_id = self.client.user.id
        _logger.debug("Getting messages for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}")
        return Message.from_json_list(response.data)

    async def send_message(self, message: Message) -> Message:
        data = message.to_json_request()
        _logger.debug("Sending message %s", json.dumps(data))
        response = await self.client.post(f"{BASE_PATH}/create", data=data)
        return Message.from_json(response.data["message"])

    async def edit_message(self, message: Message) -> Message:
        data = message.to_json_request()
        _logger.debug("Editing message %s", json.dumps(data))
        response = await self.client.put(f"{BASE_PATH}?id={message.id}", data=data)
        return Message.from_json(response.data["message"])

    async def delete_message(self, message: int | Message) -> bool:
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        _logger.debug("Deleting message %s", id)
        response = await self.client.delete(f"{BASE_PATH}/{id}")
        return True
