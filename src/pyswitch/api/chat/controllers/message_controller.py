import json
import logging
from typing import TYPE_CHECKING, List
from pyswitch.api.chat.models import Message, GroupChatHistory
from pyswitch.error import SwitchError
from pyswitch.utils.types import JSONDict
from pyswitch.api.community.models import Channel, Community, Group

if TYPE_CHECKING:
    from pyswitch.api.chat import ChatClient

_logger = logging.getLogger(__name__)

BASE_PATH = "/v1/message"


class MessageController:
    """Message controller

    This controller is used to communicate with the message endpoints.

    """

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def get_messages(self, user_id: int = None) -> List[Message]:
        """Get messages for a user

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id
        _logger.debug("Getting messages for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}")
        return Message.build_from_json_list(response.data)

    async def send_message(self, message: Message) -> Message:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent
        """
        data = message.to_json_request()
        _logger.debug("Sending message %s", json.dumps(data))
        response = await self.client.post(f"{BASE_PATH}/create", data=data)
        return Message.build_from_json(response.data["message"])

    async def edit_message(self, message: Message) -> Message:
        """Edit a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited
        """
        data = message.to_json_request()
        _logger.debug("Editing message %s", json.dumps(data))
        response = await self.client.put(f"{BASE_PATH}?id={message.id}", data=data)
        return message

    async def delete_message(self, message: int | Message) -> bool:
        """Delete a message

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message id or message to delete

        Returns:
            ``bool``: True if the message was deleted

        Raises:
            ``~switch.error.SwitchError``: If the message could not be deleted
        """
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        _logger.debug("Deleting message %s", id)
        response = await self.client.delete(f"{BASE_PATH}/{id}")
        return True

    async def delete_messages_from_user(self, recipient_id: int, user_id: int = None) -> bool:
        """Delete messages from a user

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``bool``: True if the messages were deleted

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be deleted

        """
        _logger.debug("Deleting messages for user %s", recipient_id)
        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.delete(f"{BASE_PATH}/{user_id}/{recipient_id}")
        return True

    async def get_messages_between_users(
        self, recipient_id: int, user_id: int = None, page_limit: int = 100, page_offset: int = 0
    ) -> List[Message]:
        """Get messages between two users

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
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
        """Forward a message to a group or user

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to forward
            group_channel (``~switch.api.chat.models.Group`` | ``~switch.api.chat.models.Channel`` | ``str``, *optional*): The group or channel to forward to. Defaults to None.
            receiver_id (``str``, *optional*): The user id to forward to. Defaults to None.

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be forwarded
        """
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
        """Get a message by id

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message id or message to get

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be retrieved
        """
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
        """Get group chat history

        Parameters:
            group_id (``str``): The group id
            community_id (``str``): The community id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``~switch.api.chat.models.GroupChatHistory``: The group chat history

        Raises:
            ``~switch.error.SwitchError``: If the group chat history could not be retrieved

        """
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
        """Get channel chat history

        Parameters:
            channel_id (``str``): The channel id
            community_id (``str``): The community id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``~switch.api.chat.models.ChannelChatHistory``: The channel chat history

        Raises:
            ``~switch.error.SwitchError``: If the channel chat history could not be retrieved

        """
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
        """Get community media files

        Parameters:
            community_id (``str``): The community id

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files

        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        _logger.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(f"{BASE_PATH}/media?communityId={community_id}")
        return Message.build_from_json_list(response.data)

    async def get_community_media_files_by_status(
        self, community_id: str, status: str
    ) -> List[Message]:
        """Get community media files by status

        Parameters:
            community_id (``str``): The community id
            status (``str``): The status of the media files

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files


        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        _logger.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}&status={status}"
        )
        return Message.build_from_json_list(response.data)

    async def get_user_media_files(self, user_id: int = None) -> List[Message]:
        """Get user media files


        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The user media files

        Raises:
            ``~switch.error.SwitchError``: If the user media files could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id
        _logger.debug("Getting user media files for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/media/{user_id}")
        return Message.build_from_json_list(response.data)

    async def clear_conversation(self, receiver_id: int) -> bool:
        """Clear a conversation

        Parameters:
            receiver_id (``int``): The receiver id

        Returns:
            ``bool``: True if the conversation was cleared

        Raises:
            ``~switch.error.SwitchError``: If the conversation could not be cleared
        """
        _logger.debug("Clearing conversation %s", receiver_id)
        response = await self.client.get(f"{BASE_PATH}/clearconversationwith/{receiver_id}")
        return True

    async def get_flag_messages(self, user_id: int = None) -> List[Message]:
        """Get flagged messages

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The flagged messages

        Raises:
            ``~switch.error.SwitchError``: If the flagged messages could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id

        _logger.debug("Get flag messages for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/flag?userId={user_id}")
        return Message.build_from_json_list(response.data)

    async def flag_message(self, message: Message | int) -> bool:
        """Flag a message

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to flag

        Returns:
            ``bool``: True if the message was flagged

        Raises:
            ``~switch.error.SwitchError``: If the message could not be flagged
        """
        if isinstance(message, Message):
            message_id = message.id
        else:
            message_id = message
        _logger.debug("Flagging message %s", message_id)
        response = await self.client.post(f"{BASE_PATH}/flag?messageId={message_id}")
        return True

    async def get_unread_messages_count(self, user_id: int = None) -> int:
        """Get unread messages

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``int``: The unread messages count
        """
        if user_id is None:
            user_id = self.client.user.id

        _logger.debug("Get unread messages count for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/unread-messages?userId={user_id}")
        return response.data
