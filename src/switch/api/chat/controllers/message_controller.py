import json
import logging
from typing import TYPE_CHECKING, List
from switch.api.chat.models import Message, GroupChatHistory
from switch.error import SwitchError
from switch.utils.types import JSONDict
from switch.api.community.models import Channel, Community, Group

if TYPE_CHECKING:
    from switch.api.chat import ChatClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/v1/message"


class MessageController:
    def __init__(self, client: "ChatClient"):
        self.client = client

    async def get_messages(self, user_id: int = None) -> List[Message]:
        """Get messages for a user"""
        if user_id is None:
            user_id = self.client.user.id
        _logger.debug("Getting messages for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}")
        return Message.build_from_json_list(response.data)

    async def send_message(self, message: Message) -> Message:
        """Send a message"""
        data = message.to_json_request()
        _logger.debug("Sending message %s", json.dumps(data))
        response = await self.client.post(f"{BASE_PATH}/create", data=data)
        return Message.build_from_json(response.data["message"])

    async def edit_message(self, message: Message) -> Message:
        """Edit a message"""
        data = message.to_json_request()
        _logger.debug("Editing message %s", json.dumps(data))
        response = await self.client.put(f"{BASE_PATH}?id={message.id}", data=data)
        return Message.build_from_json(response.data["message"])

    async def delete_message(self, message: int | Message) -> bool:
        """Delete a message"""
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        _logger.debug("Deleting message %s", id)
        response = await self.client.delete(f"{BASE_PATH}/{id}")
        return True

    async def delete_messages_from_user(self, recipient_id: int, user_id: int = None) -> bool:
        """Delete messages from a user"""
        _logger.debug("Deleting messages for user %s", recipient_id)
        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.delete(f"{BASE_PATH}/{user_id}/{recipient_id}")
        return True

    async def get_messages_between_users(
        self, recipient_id: int, user_id: int = None, page_limit: int = 100, page_offset: int = 0
    ) -> List[Message]:
        """Get messages from a user"""
        q = []
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        if page_offset:
            q.append(f"pageOffset={page_offset}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        _logger.debug("Getting messages for user %s", recipient_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}/{recipient_id}?{str_q}")
        return Message.build_from_json_list(response.data)

    async def forward_message(
        self,
        message: Message | int,
        group_channel: Group | Channel | str = None,
        receiver_id: str = None,
    ) -> Message:
        """Forward a message to a group or user"""
        if isinstance(message, Message):
            id = message.id
        else:
            id = message

        if isinstance(group_channel, Group):
            group_channel = group_channel.id
        elif isinstance(group_channel, Channel):
            group_channel = group_channel.id
        elif group_channel is not None:
            group_channel = group_channel

        q = []
        if group_channel is not None:
            q.append(f"groupChannelId={group_channel}")
        if receiver_id is not None:
            q.append(f"receiverId={receiver_id}")

        strQuery = q.join("&")

        _logger.debug("Forwarding message %s", id)
        response = await self.client.post(f"{BASE_PATH}/forward/{id}?{strQuery}")
        return Message.build_from_json(response.data["message"])

    async def get_message(self, message: int | Message) -> Message:
        """Get a message by id"""
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        _logger.debug("Getting message %s", id)
        response = await self.client.get(f"{BASE_PATH}/{id}")
        return Message.build_from_json(response.data["message"])

    async def get_group_chat_history(
        self,
        group_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get group chat history"""
        _logger.debug("Getting group chat history for group %s", group_id)
        q = ["isChannel=false"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(f"{BASE_PATH}/group/{user_id}/{group_id}?{str_q}")
        return GroupChatHistory.build_from_json(response.data)

    async def get_channel_chat_history(
        self,
        channel_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get channel chat history"""
        _logger.debug("Getting channel chat history for channel %s", channel_id)
        q = ["isChannel=true"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(f"{BASE_PATH}/group/{user_id}/{channel_id}?{str_q}")
        return GroupChatHistory.build_from_json(response.data)

    async def get_community_media_files(self, community_id: str) -> List[Message]:
        """Get community media files"""
        _logger.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(f"{BASE_PATH}/media?communityId={community_id}")
        return Message.build_from_json_list(response.data)

    async def get_community_media_files_by_status(
        self, community_id: str, status: str
    ) -> List[Message]:
        """Get community media files by status"""
        _logger.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}&status={status}"
        )
        return Message.build_from_json_list(response.data)

    async def get_user_media_files(self, user_id: int) -> List[Message]:
        """Get user media files"""
        if user_id is None:
            user_id = self.client.user.id
        _logger.debug("Getting user media files for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/media/{user_id}")
        return Message.build_from_json_list(response.data)

    async def clear_conversation(self, receiver_id: str) -> bool:
        """Clear a conversation"""
        _logger.debug("Clearing conversation %s", receiver_id)
        response = await self.client.get(f"{BASE_PATH}/clearconversationwith/{receiver_id}")
        return True

    async def get_flag_messages(self, user_id: int = None) -> bool:
        """Flag a message"""
        if user_id is None:
            user_id = self.client.user.id

        _logger.debug("Get flag messages for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/flag?userId={user_id}")
        return True

    async def flag_message(self, message: Message | int) -> bool:
        """Flag a message"""
        if isinstance(message, Message):
            message_id = message.id
        else:
            message_id = message
        _logger.debug("Flagging message %s", message_id)
        response = await self.client.post(f"{BASE_PATH}/flag?messageId={message_id}")
        return True

    async def get_unread_messages_count(self, user_id: int = None) -> int:
        """Get unread messages"""
        if user_id is None:
            user_id = self.client.user.id

        _logger.debug("Get unread messages count for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/unread-messages?userId={user_id}")
        return response.data
