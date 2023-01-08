import json
import logging
from typing import List
from switch.api.chat.models import Message
from switch.utils import SwitchRestClient
from switch.error import SwitchError

_logger = logging.getLogger(__name__)

BASE_PATH="/message/v1"

class MessageController:
  def __init__(self, client: SwitchRestClient):
    self.client = client

  async def get_messages(self, user_id: int = None) -> List[Message]:
    if user_id is None:
      user_id = self.client.user.id
    _logger.debug("Getting messages for user %s", user_id)
    response= await self.client.get(f"{BASE_PATH}/{user_id}") 
    return Message.from_json_list(response.data)
  
  async def send_message(self, message: Message) -> Message:
    response= await self.client.post(f"{BASE_PATH}/create", data=message.to_json())
    return Message.from_json(response.data["message"])