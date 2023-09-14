import logging
from typing import TYPE_CHECKING, List, Optional

from swibots.api.chat.models import (
    Message,
)

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/message/post"
CHAT_BASE_PATH = "/chat/v1/"


class ChatController:
    """Chat controller"""

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def pin_message(
        self,
        message: Message | int,
        detail: Optional[str] = None,
        message_type: Optional[str] = "MESSAGE",
        status: Optional[int] = None,
    ) -> bool:
        data = {"status": status, "messageType": message_type, "pinDetails": detail}
        if isinstance(message, Message):
            data |= {
                "groupId": message.group_id,
                "communityId": message.community_id,
                "channelId": message.channel_id,
                "userId": message.user_id,
                "messageId": message.id,
            }
        else:
            data["messageId"] = message
        await self.client.post(
            f"{BASE_PATH}/pin",
            data=data,
        )
        return True

    async def get_last_seen(self, user_id: int) -> int:
        response = await self.client.get(f"{CHAT_BASE_PATH}lastseen/{user_id}")
        return response.data.get("lastSeen")
