from typing import TYPE_CHECKING, BinaryIO, Callable, List, Optional, Union
from re import Match
import swibots
from io import BytesIO
from swibots.base import SwitchObject
from swibots.api.common import User, Media, EmbeddedMedia
from swibots.api.community import Community, Channel, Group
from swibots.utils.types import JSONDict
from swibots.types import MediaType
from .inline_markup import InlineMarkup


class Message(
    SwitchObject,
):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: int = None,
        user_id: int = None,
        user: "User" = None,
        receiver_id: int = None,
        receiver: "User" = None,
        message: str = None,
        matches: List[Match] = None,
        sent_date: int = None,
        status: int = None,
        request_id: int = None,
        button_name: str = None,
        button_pressed_id: int = None,
        callback_data: str = None,
        channel_chat: bool = None,
        channel_id: int = None,
        channel: "Channel" = None,
        command_name: str = None,
        community_id: int = None,
        community: "Community" = None,
        user_session_id: Optional[str] = None,
        embed_message: "EmbeddedMedia" = None,
        is_embed_message: str = None,
        edit: bool = None,
        flag: int = None,
        forward: bool = None,
        group_chat: bool = None,
        group_id: int = None,
        group: "Group" = None,
        information: str = None,
        inline_markup: "InlineMarkup" = None,
        is_read: bool = None,
        is_document: bool = None,
        media_link: str = None,
        mentioned_ids: List[int] = None,
        personal_chat: bool = None,
        pinned: bool = None,
        reactions: List[str] = None,
        replied_message: "Message" = None,
        replied_to_id: int = None,
        replied_to: "Message" = None,
        replies: List["Message"] = None,
        reply_count: int = None,
        media_id: int = None,
        link: str = None,
        media_info: Media = None,
        cached_media: Media = None,
        scheduled_at: Optional[int] = None,
        sticker_pack_id: Optional[str] = None,
        command_details: Optional[dict] = None,
        **kwargs,
    ):
        super().__init__(app=app)
        self.id = id
        self.user_id = user_id
        self.user = user
        self.receiver_id = receiver_id
        self.receiver = receiver
        self.message = message
        self.matches = matches
        self.sent_date = sent_date
        self.status = status
        self.request_id = request_id
        self.button_name = button_name
        self.button_pressed_id = button_pressed_id
        self.callback_data = callback_data
        self.channel_chat = channel_chat
        self.channel_id = channel_id
        self.channel = channel
        self.command_name = command_name
        self.community_id = community_id
        self.community = community
        self.edit = edit
        self.flag = flag
        self.forward = forward
        self.group_chat = group_chat
        self.group_id = group_id
        self.group = group
        self.information = information
        self.inline_markup = inline_markup
        self.is_read = is_read
        self.is_document = is_document
        self.media_link = media_link
        self.media_id = media_id
        self.media_info = media_info
        self.mentioned_ids = mentioned_ids
        self.personal_chat = personal_chat
        self.pinned = pinned
        self.reactions = reactions
        self.replied_message = replied_message
        self.replied_to_id = replied_to_id
        self.replied_to = replied_to
        self.replies = replies
        self.reply_count = reply_count
        self.cached_media = cached_media
        self.link = link
        self.embed_message = embed_message
        self.is_embed_message = is_embed_message
        self.scheduled_at = scheduled_at
        self.user_session_id = user_session_id
        self.sticker_pack_id = sticker_pack_id
        self.command_details = command_details
        self.__dict__.update(**kwargs)

    def to_json_request(self) -> JSONDict:
        return {
            "id": self.id,
            "message": self.message,
            "receiverId": self.receiver_id,
            "requestId": self.request_id,
            "userId": self.user_id,
            "communityId": self.community_id,
            "groupId": self.group_id,
            "channelId": self.channel_id,
            "inline_markup": (
                self.inline_markup.to_json_request() if self.inline_markup else None
            ),
            "callback_data": self.callback_data,
            "repliedTo": self.replied_to_id,
            "mediaLink": self.media_link,
            "status": 4 if self.embed_message else self.status,
            "embedMessage": (
                self.embed_message.to_json() if self.embed_message else None
            ),
            "isEmbedMessage": self.is_embed_message or bool(self.embed_message),
            "cachedMedia": self.cached_media.to_json() if self.cached_media else None,
            "mediaId": self.media_id,
            "mediaInfo": self.media_info.to_json() if self.media_info else None,
            "userSessionId": self.user_session_id,
            "link": self.link,
            "commandDetails": self.command_details,
        }

    def to_form_data(self):
        form_data = {}
        if self.user_session_id is not None:
            form_data["userSessionId"] = self.user_session_id
        if self.user_id is not None:
            form_data["userId"] = self.user_id
        if self.receiver_id is not None:
            form_data["receiverId"] = self.receiver_id
        if self.request_id is not None:
            form_data["requestId"] = self.request_id
        if self.community_id is not None:
            form_data["communityId"] = self.community_id
        if self.channel_id is not None:
            form_data["channelId"] = self.channel_id
        if self.group_id is not None:
            form_data["groupId"] = self.group_id
        if self.replied_to_id is not None:
            form_data["repliedTo"] = self.replied_to_id
        if self.message is not None:
            form_data["message"] = self.message
        if self.media_link is not None:
            form_data["mediaLink"] = self.media_link
        if self.status is not None:
            form_data["status"] = self.status
        if self.is_document is not None:
            form_data["isDocument"] = self.is_document
        if self.inline_markup is not None:
            form_data.update(self.inline_markup.to_form_data())
        if self.scheduled_at is not None:
            form_data["scheduledAt"] = self.scheduled_at
        if self.media_info is not None:
            form_data.update(self.media_info.to_form_data())
            self.media_link = self.media_info.url
        return form_data

    def to_json(self) -> JSONDict:
        replied = self.replied_message or self.replied_to
        return {
            "buttonName": self.button_name,
            "buttonPressedId": self.button_pressed_id,
            "callback_data": self.callback_data,
            "cachedMedia": self.cached_media.to_json() if self.cached_media else None,
            "channelChat": self.channel_chat,
            "channelId": self.channel_id,
            "commandName": self.command_name,
            "communityId": self.community_id,
            "edit": self.edit,
            "flag": self.flag,
            "forward": self.forward,
            "groupChat": self.group_chat,
            "groupId": self.group_id,
            "id": self.id,
            "information": self.information,
            "embedMessage": (
                self.embed_message.to_json() if self.embed_message else None
            ),
            "isEmbedMessage": self.is_embed_message,
            "inline_markup": (
                self.inline_markup.to_json() if self.inline_markup else None
            ),
            "isRead": self.is_read,
            "isDocument": self.is_document,
            "mediaLink": self.media_link,
            "mentionedIds": self.mentioned_ids,
            "message": self.message,
            "personalChat": self.personal_chat,
            "pinned": self.pinned,
            "reactions": self.reactions,
            "receiverId": self.receiver_id,
            "mediaId": self.media_id,
            "mediaInfo": self.media_info.to_json() if self.media_info else None,
            "repliedMessage": replied.to_json() if replied else None,
            "repliedTo": self.replied_to_id,
            "replies": self.replies,
            "replyCount": self.reply_count,
            "requestId": self.request_id,
            "sentDate": self.sent_date,
            "status": self.status,
            "userId": self.user_id,
            "userSessionId": self.user_session_id,
            "link": self.link,
            "commandDetails": self.command_details,
        }

    def from_json(self, data: Optional[JSONDict]) -> "Message":
        if data is not None:
            self.button_name = data.get("buttonName")
            self.button_pressed_id = data.get("buttonPressedId")
            self.callback_data = data.get("callback_data")
            self.channel_chat = data.get("channelChat")
            self.channel_id = data.get("channelId")
            self.channel = Channel.build_from_json(data.get("channel"), self.app)
            self.command_name = data.get("commandName")
            self.community_id = data.get("communityId")
            self.community = Community.build_from_json(data.get("community"), self.app)
            self.edit = data.get("edit")
            self.flag = data.get("flag")
            self.forward = data.get("forward")
            self.group_chat = data.get("groupChat")
            self.group_id = data.get("groupId")
            self.group = Group.build_from_json(data.get("group"), self.app)
            self.id = data.get("id")
            self.information = data.get("information")
            self.inline_markup = InlineMarkup.build_from_json(
                data.get("inline_markup"), self.app
            )
            self.link = data.get("link")
            self.is_read = data.get("isRead")
            self.is_document = data.get("isDocument")
            self.media_link = data.get("mediaLink")
            self.media_id = data.get("mediaId")
            self.media_info: Media = Media.build_from_json(
                data.get("mediaInfo"), self.app
            )
            if self.media_info:
                if not self.media_id:
                    self.media_id = self.media_info.id
                if not self.media_link:
                    self.media_link = self.media_info.url
            self.cached_media = Media.build_from_json(data.get("cachedMedia"), self.app)
            self.mentioned_ids = data.get("mentionedIds")
            self.message = data.get("message")
            self.personal_chat = data.get("personalChat")
            self.pinned = data.get("pinned")
            self.reactions = data.get("reactions")
            self.command_details = data.get("commandDetails")
            receiver_id = data.get("receiverId", 0)
            if receiver_id == "null":
                receiver_id = 0
            self.receiver_id = int(receiver_id)
            self.replied_to = Message.build_from_json(
                data.get("repliedMessage"), self.app
            )
            self.replied_to_id = data.get("repliedTo")
            self.replies = data.get("replies")
            self.reply_count = data.get("replyCount")
            self.request_id = data.get("requestId")
            self.sent_date = data.get("sentDate")
            self.status = data.get("status")

            self.user = User.build_from_json(data.get("senderInfo"), self.app)
            self.user_id = int(data.get("userId", 0))
            self.embed_message = EmbeddedMedia.build_from_json(
                data.get("embedMessage"), self.app
            )
            self.is_embed_message = data.get("isEmbedMessage") == "true" or bool(
                self.embed_message
            )
            self.user_session_id = data.get("userSessionId")
            self.sticker_pack_id = data.get("stickerPackId")
        return self

    @property
    def chat_id(self):
        return self.user_session_id or self.channel_id or self.group_id or self.user_id

    @property
    def is_media(self):
        # 1 = IMAGE
        # 2 = Video
        # 3 = AUDIO
        # 7 = FILE
        return self.status in [1, 2, 3, 7]

    @property
    def video(self):
        """Whether message includes video"""
        return self.media_info and self.media_info.media_type == MediaType.VIDEO.value

    @property
    def photo(self):
        """Whether message includes photo"""
        return self.media_info and self.media_info.media_type == MediaType.IMAGE.value

    @property
    def audio(self):
        """Whether message includes audio as media"""
        return self.media_info and self.media_info.media_type == MediaType.AUDIO.value

    @property
    def document(self):
        """Whether message includes document"""
        return (
            self.media_info and self.media_info.media_type == MediaType.DOCUMENT.value
        )

    @property
    def sticker(self):
        """Whether message is sticker"""
        return bool(self.sticker_pack_id)

    async def get_replies(self) -> List["Message"]:
        if self.reply_count <= 0:
            return []
        if self.replies is None:
            self.replies = await self.app.get_message_replies(self.id)
        return self.replies

    async def get_replied_message(self) -> "Message":
        if self.replied_message:
            return self.replied_message
        if self.replied_to_id is None or self.replied_to_id <= 0:
            return None
        if self.replied_to is None:
            self.replied_to = await self.app.get_message(self.replied_to_id)
        return self.replied_to

    def _get_receiver_id(self):
        """Get receiver id to send message"""
        if not self.personal_chat:
            return
        return self.user_id if self.user_id != self.app.user.id else self.receiver_id

    ### API Methods ###

    async def respond(
        self,
        message: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
        **kwargs,
    ) -> "Message":
        return await self.app.send_message(
            message=message,
            community_id=self.community_id,
            group_id=self.group_id,
            channel_id=self.channel_id,
            user_id=self._get_receiver_id(),
            user_session_id=self.user_session_id,
            embed_message=embed_message,
            inline_markup=inline_markup,
            **kwargs,
        )

    send = respond

    async def delete(self) -> None:
        return await self.app.delete_message(self)

    async def reply_text(
        self,
        message: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
        quote: bool = None,
        **kwargs,
    ) -> "Message":
        if quote == None:
            quote = True if self.personal_chat else False

        return await self.app.send_message(
            message,
            community_id=self.community_id,
            group_id=self.group_id,
            channel_id=self.channel_id,
            user_id=self._get_receiver_id(),
            reply_to_message_id=self.id if quote else None,
            user_session_id=self.user_session_id,
            embed_message=embed_message,
            inline_markup=inline_markup,
            **kwargs,
        )

    async def reply_media(
        self,
        document: Union[str, BytesIO],
        message: str = "",
        thumb: Union[str, BytesIO] = None,
        progress=None,
        progress_args=None,
        inline_markup: InlineMarkup = None,
        quote: bool = None,
        **kwargs,
    ) -> "Message":
        """reply media to the message"""
        if quote == None:
            quote = True if self.personal_chat else False
        return await self.app.send_media(
            message=message,
            document=document,
            community_id=self.community_id,
            group_id=self.group_id,
            channel_id=self.channel_id,
            user_id=self._get_receiver_id(),
            thumb=thumb,
            user_session_id=self.user_session_id,
            reply_to_message_id=self.id if quote else None,
            progress=progress,
            progress_args=progress_args,
            inline_markup=inline_markup,
            **kwargs,
        )

    async def edit_inline_markup(self, inline_markup: InlineMarkup = None):
        """Edit inline markup of message"""
        if not inline_markup:
            inline_markup = InlineMarkup()
        return await self.edit_text(text=None, inline_markup=inline_markup)

    async def edit_media(
        self,
        document: str,
        message: Optional[str] = None,
        inline_markup: Optional[InlineMarkup] = None,
        **kwargs,
    ):
        """Bound method of client.edit_media

        Args:
           document: path to file
           message: message caption
           inline_markup: InlineMarkup
        """
        return await self.app.edit_media(
            message_id=self.id,
            media_id=self.media_id,
            document=document,
            message=message,
            inline_markup=inline_markup,
            **kwargs,
        )

    async def reply_document(
        self,
        document: Union[str, BytesIO],
        message: str = "",
        thumb: Union[str, BytesIO] = None,
        progress=None,
        progress_args=None,
        inline_markup: InlineMarkup = None,
        quote: bool = None,
        **kwargs,
    ) -> "Message":
        """Reply document to the message"""
        return await self.reply_media(
            message=message,
            document=document,
            media_type=MediaType.DOCUMENT.value,
            thumb=thumb,
            progress=progress,
            progress_args=progress_args,
            inline_markup=inline_markup,
            quote=quote,
            **kwargs,
        )

    async def reply_audio(
        self,
        audio: Union[str, BytesIO],
        caption: str = "",
        inline_markup: InlineMarkup = None,
        quote: bool = None,
        **kwargs,
    ):
        """Reply audio to message!"""
        return await self.reply_media(
            message=caption,
            document=audio,
            media_type=MediaType.AUDIO.value,
            inline_markup=inline_markup,
            quote=quote,
            **kwargs,
        )

    async def edit_text(
        self,
        text: str,
        embed_message: EmbeddedMedia = None,
        inline_markup: Optional[InlineMarkup] = None,
        **kwargs,
    ) -> "Message":
        if not inline_markup:
            inline_markup = self.inline_markup

        return await self.app.edit_message_text(
            self.id,
            text,
            embed_message=embed_message,
            inline_markup=inline_markup,
            **kwargs,
        )

    async def listen(self, *args, **kwargs):
        """Listen for messages in current chat"""
        return await self.app.listen_messages(self.chat_id, *args, **kwargs)

    async def forward_to(
        self,
        group_channel: Union[Group, Channel, str] = None,
        user_id: Optional[int] = None,
    ):
        return await self.app.forward_message(self.id, group_channel, user_id)

    async def download(
        self,
        file_name: str = None,
        in_memory: bool = False,
        block: bool = True,
        progress: Callable = None,
        progress_args: tuple = (),
    ) -> Optional[Union[BinaryIO, bytes]]:
        if not file_name and self.media_info:
            file_name = self.media_info.description
        return await self.app.download_media(
            self, file_name, in_memory, block, progress, progress_args
        )
