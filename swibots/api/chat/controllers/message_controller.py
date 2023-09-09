import asyncio
import mimetypes
import os
import json
from inspect import iscoroutinefunction
import logging
from typing import TYPE_CHECKING, List, Optional
from io import BytesIO
from asyncio.tasks import Task
from swibots.errors import CancelError
from swibots.api.chat.models import (
    Message,
    GroupChatHistory,
    InlineMarkup,
    InlineQuery,
    InlineQueryAnswer,
)
from swibots.api.common.models import User, EmbeddedMedia
from swibots.api.community.models import Channel, Group

from swibots.utils.types import (
    IOClient,
    ReadCallbackStream,
    UploadProgress,
)

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/message"


class MessageController:
    """Message controller

    This controller is used to communicate with the message endpoints.

    """

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def new_message(
        self,
        to: Optional[int | User] = None,
        channel: Optional[Channel | str] = None,
        group: Optional[Group | str] = None,
    ) -> Message:
        """Create a new message"""
        if isinstance(to, User):
            to = to.id

        if isinstance(channel, Channel):
            channel = channel.id

        if isinstance(group, Group):
            group = group.id

        return Message(
            user_id=self.client.user.id,
            receiver_id=to,
            channel_id=channel,
            group_id=group,
            app=self.client.app,
        )

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
        log.debug("Getting messages for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}")
        return self.client.build_list(Message, response.data)

    async def send_message(
        self,
        message: str,
        community_id: str = None,
        channel_id: str = None,
        group_id: str = None,
        user_id: Optional[int] = None,
        document: Optional[str | BytesIO] = None,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        embed_message: Optional[EmbeddedMedia] = None,
        inline_markup: Optional[InlineMarkup] = None,
        reply_to_message_id: Optional[int] = None,
        scheduled_at: Optional[int] = None,
        **kwargs,
    ) -> Message | Task:
        if not (user_id or (community_id and (group_id or channel_id))):
            raise ValueError(
                "No chat parameter provided, Either use user_id or group_id/channel_id with community_id."
            )
        if document:
            return await self.send_media(
                document=document,
                message=message,
                caption=caption,
                description=description,
                community_id=community_id,
                group_id=group_id,
                channel_id=channel_id,
                user_id=user_id,
                scheduled_at=scheduled_at,
                **kwargs,
            )

        new_message = Message(
            app=self.client.app,
            message=message,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            receiver_id=user_id,
            embed_message=embed_message,
            inline_markup=inline_markup,
            replied_to_id=reply_to_message_id,
            scheduled_at=scheduled_at,
            **kwargs,
        )

        if new_message.embed_message and new_message.embed_message.thumbnail:
            thumb = new_message.embed_message.thumbnail
            if thumb and os.path.exists(thumb):
                new_message.embed_message.thumbnail = (
                    await self.client.app.upload_media(thumb)
                ).url

        data = new_message.to_json_request()
        log.debug("Sending message %s", json.dumps(data))

        response = await self.client.post(f"{BASE_PATH}/create", data=data)
        return self.client.build_object(Message, response.data["message"])

    async def send_media(
        self,
        document: Optional[str | BytesIO] = None,
        message: Optional[str] = "",
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        user_id: Optional[int] = None,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        thumb: Optional[str | BytesIO] = None,
        blocking: Optional[bool] = True,
        progress: Optional[callable] = None,
        progress_args: Optional[tuple] = (),
        reply_to_message_id: Optional[int] = None,
        scheduled_at: Optional[int] = None,
        **kwargs,
    ) -> Message | Task:
        new_message = Message(
            app=self.client.app,
            receiver_id=user_id,
            community_id=community_id,
            group_id=group_id,
            channel_id=channel_id,
            replied_to_id=reply_to_message_id,
            message=message,
            scheduled_at=scheduled_at,
            **kwargs,
        )
        form = new_message.to_form_data()
        files = {}
        log.debug("Sending message %s", json.dumps(form))
        request_url = f"{BASE_PATH}/create-with-media"
        reader, thumb_like = None, None
        name = document if isinstance(document, str) else document.name
        reader = ReadCallbackStream(document, None)
        files["uploadMediaRequest.file"] = (
            file_name or name,
            reader,
            mime_type,
        )
        form.update(
            {
                "uploadMediaRequest.caption": caption or file_name or name,
                "uploadMediaRequest.description": description or file_name or name,
                "uploadMediaRequest.mimeType": mime_type
                or (
                    mimetypes.guess_type(name)[0]
                )
                or "application/octet-stream",
            }
        )

        if progress:
            d_progress = UploadProgress(
                current=0,
                readed=0,
                file_name=document if isinstance(document, str) else document.name,
                client=IOClient(),
                url=request_url,
                callback=progress,
                callback_args=progress_args,
            )
            reader.callback = d_progress.update
            d_progress._readable_file = reader

        if thumb:
            _is_path = isinstance(thumb, str)
            thumb_like = open(thumb, "rb") if _is_path else thumb
            thumb_name = thumb if _is_path else thumb.name
            files["uploadMediaRequest.thumbnail"] = (
                thumb_name,
                thumb_like,
                mimetypes.guess_type(thumb_name)[0],
            )

        def close_files(_task=None):
            if reader:
                reader.close()
            if thumb_like:
                thumb_like.close()

        request = self.client.post(request_url, files=files or None, form_data=form)
        task = asyncio.get_event_loop().create_task(request)
        if not blocking:
            task.add_done_callback(close_files)
            return task
        response = await task
        close_files()
        return self.client.build_object(Message, response.data["message"])

    async def edit_message(
        self,
        message_id: int,
        text: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
        **kwargs,
    ) -> Message:
        """Edit a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited
        """
        new_message = Message(
            self.client.app,
            message=text,
            inline_markup=inline_markup,
            id=message_id,
            **kwargs,
        )

        if embed_message:
            if embed_message.thumbnail and os.path.exists(embed_message.thumbnail):
                response_media = await self.client.app.upload_media(
                    embed_message.thumbnail
                )
                embed_message.thumbnail = response_media.url
            new_message.embed_message = embed_message

        data = new_message.to_json_request()
        log.debug("Editing message %s", json.dumps(data))
        response = await self.client.put(f"{BASE_PATH}?id={message_id}", data=data)
        return self.client.build_object(Message, response.data["message"])

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
        log.debug("Deleting message %s", id)
        response = await self.client.delete(f"{BASE_PATH}/{id}")
        return True

    async def delete_messages_from_user(
        self, recipient_id: int, user_id: int = None
    ) -> bool:
        """Delete messages from a user

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``bool``: True if the messages were deleted

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be deleted

        """
        log.debug("Deleting messages for user %s", recipient_id)
        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.delete(f"{BASE_PATH}/{user_id}/{recipient_id}")
        return True

    async def get_messages_between_users(
        self,
        recipient_id: int,
        user_id: int = None,
        page_limit: int = 100,
        page_offset: int = 0,
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

        log.debug("Getting messages for user %s", recipient_id)
        response = await self.client.get(
            f"{BASE_PATH}/{user_id}/{recipient_id}?{str_q}"
        )
        return self.client.build_list(Message, response.data["messages"])

    async def forward_message(
        self,
        message_id: int | List[int],
        group_channel: Optional[Group | Channel | str] = None,
        user_id: Optional[int] = None,
    ) -> Message | List[Message]:
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
        if isinstance(group_channel, (Group, Channel)):
            group_channel = group_channel.id
        elif group_channel is not None:
            group_channel = group_channel

        if isinstance(message_id, list):
            message_id = ",".join(message_id)

        q = []
        if group_channel is not None:
            q.append(f"groupChannelId={group_channel}")
        if user_id is not None:
            q.append(f"receiverId={user_id}")

        strQuery = "&".join(q)

        log.debug("Forwarding message %s", id)
        response = await self.client.put(f"{BASE_PATH}/forward/{message_id}?{strQuery}")
        if isinstance(response.data, list):
            message = self.client.build_list(Message, response.data)
        if isinstance(message_id, list):
            return message
        return message[0] if message else None

    async def get_message(self, message_id: int) -> Message:
        """Get a message by id

        Parameters:
            message_id (``int``): The message id

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be retrieved
        """
        log.debug("Getting message %s", message_id)
        response = await self.client.get(f"{BASE_PATH}/findOne/{message_id}")
        return self.client.build_object(Message, response.data)

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
        log.debug("Getting group chat history for group %s", group_id)
        q = ["isChannel=false"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        else:
            q.append(f"pageLimit=0")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        else:
            q.append(f"pageOffset=0")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(
            f"{BASE_PATH}/group/{user_id}/{group_id}?{str_q}"
        )
        return self.client.build_object(GroupChatHistory, response.data)

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
        log.debug("Getting channel chat history for channel %s", channel_id)
        q = ["isChannel=true"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        else:
            q.append(f"pageLimit=0")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        else:
            q.append(f"pageOffset=0")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(
            f"{BASE_PATH}/group/{user_id}/{channel_id}?{str_q}"
        )
        return self.client.build_object(GroupChatHistory, response.data)
        # return GroupChatHistory.build_from_json(response.data)

    async def get_community_media_files(self, community_id: str) -> List[Message]:
        """Get community media files

        Parameters:
            community_id (``str``): The community id

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files

        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        log.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}"
        )
        return self.client.build_list(Message, response.data)

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
        log.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}&status={status}"
        )
        return self.client.build_list(Message, response.data)

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
        log.debug("Getting user media files for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/media/{user_id}")
        return self.client.build_list(Message, response.data)
        # return Message.build_from_json_list(response.data)

    async def clear_conversation(self, receiver_id: int) -> bool:
        """Clear a conversation

        Parameters:
            receiver_id (``int``): The receiver id

        Returns:
            ``bool``: True if the conversation was cleared

        Raises:
            ``~switch.error.SwitchError``: If the conversation could not be cleared
        """
        log.debug("Clearing conversation %s", receiver_id)
        response = await self.client.get(
            f"{BASE_PATH}/clearconversationwith/{receiver_id}"
        )
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

        log.debug("Get flag messages for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/flag?userId={user_id}")
        return self.client.build_list(Message, response.data)

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
        log.debug("Flagging message %s", message_id)
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

        log.debug("Get unread messages count for %s", user_id)
        response = await self.client.get(
            f"{BASE_PATH}/unread-messages?userId={user_id}"
        )
        return response.data

    async def answer_inline_query(
        self, query: InlineQuery, answer: InlineQueryAnswer
    ) -> bool:
        """Answer an inline query

        Parameters:
            query (``~switch.api.chat.models.InlineQuery``): The inline query
            answer (``~switch.api.chat.models.InlineQueryAnser``): The answer

        Returns:
            ``bool``: True if the query was answered

        Raises:
            ``~switch.error.SwitchError``: If the query could not be answered
        """
        if not isinstance(query, InlineQuery):
            raise TypeError("query must be an InlineQuery instance")

        if isinstance(answer, str):
            answer = InlineQueryAnswer(
                query_id=query.query_id,
                title=answer,
                results=[],
                cache_time=0,
                is_personal=True,
                next_offset=None,
                pm_text=None,
                pm_parameter=None,
                user_id=query.user_id,
            )

        if isinstance(answer, List):
            answer = InlineQueryAnswer(
                query_id=query.query_id,
                title=None,
                results=answer,
                cache_time=0,
                is_personal=True,
                next_offset=None,
                pm_text=None,
                pm_parameter=None,
                user_id=query.user_id,
            )

        if not answer.user_id:
            answer.user_id = query.user_id

        log.debug("Answering inline query %s", query.query_id)
        response = await self.client.post(
            f"{BASE_PATH}/inline/answer", answer.to_json_request()
        )
        return response.data

    async def get_user(self, user_id: int | str = None) -> User:
        """Get user from user id"""
        response = await self.client.get(f"{BASE_PATH}/user/info?userId={user_id}")
        return self.client.build_object(User, response.data)
