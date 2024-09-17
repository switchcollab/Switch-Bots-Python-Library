import asyncio
import os
import json
import logging
from typing import TYPE_CHECKING, List, Optional, Tuple, Union
from urllib.parse import urlencode
from io import BytesIO
from asyncio.tasks import Task
from swibots.types import MediaType
from swibots.api.chat.models import (
    Message,
    GroupChatHistory,
    InlineMarkup,
    InlineQuery,
    InlineQueryAnswer,
)
from swibots.utils import isUrl
from swibots.api.common.models import User, EmbeddedMedia, Media
from swibots.api.community.models import Channel, Group

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

    async def get_messages(
        self, user_id: int = None, limit: int = 100, offset: int = 0
    ) -> List[Message]:
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
        data = {"limit": limit, "offset": offset}
        log.debug("Getting messages for user %s", user_id)
        response = await self.client.get(
            f"{BASE_PATH}/personal/{user_id}?{urlencode(data)}"
        )
        return self.client.build_list(Message, response.data)

    async def send_message(
        self,
        message: str,
        community_id: str = None,
        channel_id: str = None,
        group_id: str = None,
        user_id: Optional[int] = None,
        user_session_id: Optional[str] = None,
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
                user_session_id=user_session_id,
                inline_markup=inline_markup,
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
            user_session_id=user_session_id,
            embed_message=embed_message,
            inline_markup=inline_markup,
            replied_to_id=reply_to_message_id,
            scheduled_at=scheduled_at,
            **kwargs,
        )

        if new_message.embed_message:
            if new_message.embed_message.thumbnail:
                thumb = new_message.embed_message.thumbnail
                if thumb and not isUrl(thumb):
                    new_message.embed_message.thumbnail = (
                        await self.client.app.upload_media(thumb)
                    ).url

        data = new_message.to_json_request()
        log.debug("Sending message %s", json.dumps(data))
        response = await self.client.post(f"{BASE_PATH}/create", data=data)
        return self.client.build_object(Message, response.data["message"])

    async def send_media(
        self,
        document: str = None,
        media: Optional[Media] = None,
        message: Optional[str] = "",
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        user_id: Optional[int] = None,
        user_session_id: Optional[str] = None,
        caption: Optional[str] = None,
        description: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        media_type: Optional[int] = None,
        thumb: Optional[str | BytesIO] = None,
        blocking: Optional[bool] = True,
        progress: Optional[callable] = None,
        progress_args: Optional[tuple] = (),
        reply_to_message_id: Optional[int] = None,
        scheduled_at: Optional[int] = None,
        inline_markup: Optional[InlineMarkup] = None,
        part_size: Optional[int] = None,
        task_count: Optional[int] = None,
        premium: Optional[bool] = False,
        **kwargs,
    ) -> Message | Task:
        async def _upload_media(media):
            if document:
                force_storage_method = kwargs.get("secondary_upload", False)
                private_community = None
                if community_id:
                    community = await self.client.app.get_community(community_id)
                    private_community = not community.is_public

                media = await self.client.app.upload_media(
                    path=document,
                    caption=caption,
                    description=(
                        file_name or description or os.path.basename(document)
                        if isinstance(document, str)
                        else document.name
                    ),
                    mime_type=mime_type,
                    media_type=media_type,
                    callback=progress,
                    callback_args=progress_args,
                    thumb=thumb,
                    part_size=part_size,
                    task_count=task_count,
                    premium=premium,
                    for_document=kwargs.get("is_document")
                    or (kwargs.get("media_type", 0) == MediaType.DOCUMENT.value),
                    private_community=private_community or force_storage_method,
                )
            elif not media:
                raise ValueError("'media' or 'document' must be provided!")
            new_message = Message(
                app=self.client.app,
                receiver_id=user_id,
                community_id=community_id,
                group_id=group_id,
                channel_id=channel_id,
                user_session_id=user_session_id,
                media_info=media,
                replied_to_id=reply_to_message_id,
                message=message,
                inline_markup=inline_markup,
                media_link=media.url if media else None,
                scheduled_at=scheduled_at,
                **kwargs,
            )
            form = new_message.to_json_request()
            log.debug("Sending message %s", json.dumps(form))
            request_url = f"{BASE_PATH}/create"
            response = await self.client.post(request_url, data=form)
            return self.client.build_object(Message, response.data["message"])

        task = asyncio.create_task(_upload_media(media))
        if blocking:
            return await task
        return task

    async def edit_media(
        self,
        message_id: int,
        media_id: Optional[int] = None,
        message: Optional[str] = None,
        document: Optional[str] = None,
        thumb: Optional[str] = None,
        inline_markup: InlineMarkup = None,
        progress=None,
        progress_args: Optional[Tuple] = None,
        mime_type: Optional[str] = None,
        file_name: Optional[str] = None,
        **kwargs,
    ) -> Union[Message, Media]:
        msg = None
        if message_id:
            msg = await self.client.app.get_message(message_id)
            media_id = msg.media_id
            if not media_id:
                raise ValueError("Message does'nt contain any media!")
        if document:
            media = await self.client.app.upload_media(
                path=document,
                caption=message,
                thumb=thumb,
                callback=progress,
                callback_args=progress_args,
                part_size=kwargs.get("part_size"),
                task_count=kwargs.get("task_count"),
                mime_type=mime_type,
                description=(
                    file_name or os.path.basename(document) if document else None
                ),
            )
        else:
            media = Media(
                app=self.client.app,
                description=file_name,
                file_name=file_name,
                thumbnail_url=thumb,
                mime_type=mime_type,
            )
        log.debug(f"response from [upload_media]: {media}")
        response = await self.client.app.update_media_info(
            media_id=media_id, media=media
        )
        log.debug(f"response from [update_media_info]:{response}")
        if not message_id:
            return response
        response = await self.edit_message(
            message_id=message_id,
            text=message,
            inline_markup=inline_markup,
            media_id=media_id,
            **kwargs,
        )
        response.media_info = await self.client.app.get_media(media_id)
        return response

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
        new_message = await self.client.app.get_message(message_id)
        if text is not None:
            new_message.message = text
        if inline_markup:
            new_message.inline_markup = inline_markup
        for key, value in kwargs.items():
            setattr(new_message, key, value)

        if embed_message is not None:
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

    async def delete_messages(self, message_ids: List[Union[int, Message]]) -> bool:
        """Delete a message

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message id or message to delete

        Returns:
            ``bool``: True if the message was deleted

        Raises:
            ``~switch.error.SwitchError``: If the message could not be deleted
        """
        message_ids = ",".join(
            [
                str(message.id if isinstance(message, Message) else message)
                for message in message_ids
            ]
        )
        log.debug(f"Deleting message {message_ids}")
        response = await self.client.delete(f"{BASE_PATH}/{message_ids}")
        log.debug(response)
        return True

    async def delete_messages_from_user(self, receiver_id: int) -> bool:
        """Delete messages from a user

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``bool``: True if the messages were deleted

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be deleted

        """
        log.debug("Deleting messages for user %s", receiver_id)
        response = await self.client.delete(
            f"{BASE_PATH}/clear-personal-messages?receiverId={receiver_id}"
        )
        return True

    async def get_messages_between_users(
        self,
        other_user_id: int,
        user_id: int = None,
        page_limit: int = 100,
        page_offset: int = 0,
    ) -> List[Message]:
        """Get messages between two users

        Parameters:
            other_user_id (``int``): The other user id.
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
        data = {
            "pageOffset": page_offset,
            "pageLimit": page_limit,
        }

        if user_id is None:
            user_id = self.client.user.id

        log.debug("Getting messages for user %s", other_user_id)
        response = await self.client.get(
            f"{BASE_PATH}/{user_id}/{other_user_id}?{urlencode(data)}"
        )
        return self.client.build_list(Message, response.data)

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
        message_id_list = isinstance(message_id, list)

        if message_id_list:
            message_id = ",".join(map(str, message_id))

        q = []
        if group_channel is not None:
            q.append(f"groupChannelId={group_channel}")
        if user_id:
            q.append(f"receiverId={user_id}")

        strQuery = "&".join(q)

        log.debug("Forwarding message %s", id)
        response = await self.client.put(f"{BASE_PATH}/forward/{message_id}?{strQuery}")
        message = self.client.build_list(
            Message, [data.get("message") for data in response.data]
        )
        if message_id_list:
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
        data = {
            "communityId": community_id,
            "offset": page_offset,
            "limit": page_limit,
            "groupId": group_id,
        }
        response = await self.client.get(
            f"{BASE_PATH}/community-messages?{urlencode(data)}"
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
        data = {
            "communityId": community_id,
            "pageOffset": page_offset,
            "pageLimit": page_limit,
            "channelId": channel_id,
        }

        response = await self.client.get(
            f"{BASE_PATH}/community-messages?{urlencode(data)}"
        )
        return self.client.build_object(GroupChatHistory, response.data)

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
        return self.client.build_list(Message, response.data.get("result"))

    async def get_community_media_files_by_status(
        self,
        *,
        status: Union[str, List[str]],
        community_id: str = None,
        channel_id: str = None,
        user_id: int = None,
        group_id: str = None,
    ) -> List[Message]:
        """Get community media files by status

        Parameters:
            community_id (``str``): The community id
            channel_id (``str``)
            group_id (``str``)
            user_id (``int``)
            status (``str``): The status of the media files

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files


        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        log.debug("Getting community media files for community %s", community_id)
        if not isinstance(status, list):
            status = [status]
        params = urlencode(
            {
                x: y
                for x, y in {
                    "communityId": community_id,
                    "groupId": group_id,
                    "receiverId": user_id,
                    "status": ",".join(list(map(str, status))),
                    "channelId": channel_id,
                }.items()
                if y
            }
        )
        response = await self.client.get(f"{BASE_PATH}/mediabystatus?{params}")
        return self.client.build_list(Message, response.data.get("result"))

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

    async def get_user(self, user_id: int | str = None, username: str = None) -> User:
        """Get user from user id or username"""
        if username and user_id:
            raise ValueError("'username' and 'user_id' both were provided!")
        elif user_id:
            response = await self.client.app.auth_service.get(
                f"/api/users/getUserById?userid={user_id}"
            )
        elif username:
            if username.startswith("@"):
                username = username[1:]
            response = await self.client.app.auth_service.get(
                f"/api/users/getUserByUsername?username={username}"
            )
            if not response.data:
                return
        else:
            raise ValueError("Either provide 'user_id' or 'username' to get user info.")
        return self.client.build_object(User, response.data)
