from typing import TYPE_CHECKING, List, Optional
import swibots
from swibots.base import SwitchObject
from swibots.api.common import User
from swibots.api.community import Community, Channel, Group
from swibots.utils.types import JSONDict
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
        edit: bool = None,
        flag: int = None,
        forward: bool = None,
        group_chat: bool = None,
        group_id: int = None,
        group: "Group" = None,
        information: str = None,
        inline_markup: "InlineMarkup" = None,
        is_read: bool = None,
        media_link: str = None,
        mentioned_ids: List[int] = None,
        personal_chat: bool = None,
        pinned: bool = None,
        reactions: List[str] = None,
        replied_message: str = None,
        replied_to_id: int = None,
        replied_to: "Message" = None,
        replies: List["Message"] = None,
        reply_count: int = None,
        **kwargs,
    ):
        super().__init__(app=app)
        self.id = id
        self.user_id = user_id
        self._user = user
        self.receiver_id = receiver_id
        self._receiver = receiver
        self.message = message
        self.sent_date = sent_date
        self.status = status
        self.request_id = request_id
        self.button_name = button_name
        self.button_pressed_id = button_pressed_id
        self.callback_data = callback_data
        self.channel_chat = channel_chat
        self.channel_id = channel_id
        self._channel = channel
        self.command_name = command_name
        self.community_id = community_id
        self._community = community
        self.edit = edit
        self.flag = flag
        self.forward = forward
        self.group_chat = group_chat
        self.group_id = group_id
        self.group = group
        self.information = information
        self.inline_markup = inline_markup
        self.is_read = is_read
        self.media_link = media_link
        self.mentioned_ids = mentioned_ids
        self.personal_chat = personal_chat
        self.pinned = pinned
        self.reactions = reactions
        self.replied_message = replied_message
        self.replied_to_id = replied_to_id
        self._replied_to = replied_to
        self._replies = replies
        self.reply_count = reply_count
        self.__dict__.update(**kwargs)

    def to_json_request(self) -> JSONDict:
        return {
            "id": self.id,
            "message": self.message,
            "receiverId": self.receiver_id,
            "requestId": self.request_id,
            "userId": self.user_id,
            "inline_markup": self.inline_markup.to_json_request() if self.inline_markup else None,
            "callback_data": self.callback_data,
            "repliedToId": self.replied_to_id,
            "status": self.status,
        }

    def to_json(self) -> JSONDict:
        return {
            "buttonName": self.button_name,
            "buttonPressedId": self.button_pressed_id,
            "callback_data": self.callback_data,
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
            "inline_markup": self.inline_markup.to_json() if self.inline_markup else None,
            "isRead": self.is_read,
            "mediaLink": self.media_link,
            "mentionedIds": self.mentioned_ids,
            "message": self.message,
            "personalChat": self.personal_chat,
            "pinned": self.pinned,
            "reactions": self.reactions,
            "receiverId": self.receiver_id,
            "repliedMessage": self.replied_message,
            "repliedToId": self.replied_to_id,
            "replies": self.replies,
            "replyCount": self.reply_count,
            "requestId": self.request_id,
            "sentDate": self.sent_date,
            "status": self.status,
            "userId": self.user_id,
        }

    def from_json(self, data: Optional[JSONDict]) -> "Message":
        if data is not None:
            self.button_name = data.get("buttonName")
            self.button_pressed_id = data.get("buttonPressedId")
            self.callback_data = data.get("callback_data")
            self.channel_chat = data.get("channelChat")
            self.channel_id = data.get("channelId")
            self.command_name = data.get("commandName")
            self.community_id = data.get("communityId")
            self.edit = data.get("edit")
            self.flag = data.get("flag")
            self.forward = data.get("forward")
            self.group_chat = data.get("groupChat")
            self.group_id = data.get("groupId")
            self.id = data.get("id")
            self.information = data.get("information")
            self.inline_markup = InlineMarkup.build_from_json(
                data.get("inline_markup"), self.app)
            self.is_read = data.get("isRead")
            self.media_link = data.get("mediaLink")
            self.mentioned_ids = data.get("mentionedIds")
            self.message = data.get("message")
            self.personal_chat = data.get("personalChat")
            self.pinned = data.get("pinned")
            self.reactions = data.get("reactions")
            self.receiver_id = data.get("receiverId")
            self.replied_message = data.get("repliedMessage")
            self.replied_to_id = data.get("repliedToId")
            self.replies = data.get("replies")
            self.reply_count = data.get("replyCount")
            self.request_id = data.get("requestId")
            self.sent_date = data.get("sentDate")
            self.status = data.get("status")
            self.user_id = data.get("userId")
        return self

    @property
    async def sender(self) -> "User":
        if self.user_id is None:
            return None
        if self._user is None:
            self._user = await self.app.get_user(self.user_id)
        return self._user

    @property
    async def _receiver(self) -> "User":
        if self.receiver_id is None:
            return None
        if self._receiver is None:
            self._receiver = await self.app.get_user(self.receiver_id)
        return self._receiver

    @property
    async def group(self) -> "Group":
        if self.group_id is None:
            return None
        if self.group is None:
            self.group = await self.app.get_group(self.group_id)
        return self.group

    @property
    async def _channel(self) -> "Channel":
        if self.channel_id is None:
            return None
        if self._channel is None:
            self._channel = await self.app.get_channel(self.channel_id)
        return self._channel

    @property
    async def _community(self) -> "Community":
        if self.community_id is None:
            return None
        if self._community is None:
            self._community = await self.app.get_community(self.community_id)
        return self._community

    @property
    async def _replied_to(self) -> "Message":
        if self.replied_to_id is None or self.replied_to_id <= 0:
            return None
        if self._replied_to is None:
            self._replied_to = await self.app.get_message(self.replied_to_id)
        return self._replied_to

    @property
    async def replies(self) -> List["Message"]:
        if self.reply_count <= 0:
            return []
        if self._replies is None:
            self._replies = await self.app.get_message_replies(self.id)
        return self._replies

    ### API Methods ###

    async def send(self) -> "Message":
        if self.id is not None:
            return await self.app.edit_message(self)
        return await self.app.send_message(self)

    async def delete(self) -> None:
        await self.app.delete_message(self)

    async def reply(self, reply: "Message") -> "Message":
        return await self.app.reply_message(self, reply)

    async def reply_text(self, text: str, inline_markup: Optional[InlineMarkup] = None) -> "Message":
        return await self.app.reply_message_text(self, text, inline_markup)

    async def edit_text(self, text: str,  inline_markup: Optional[InlineMarkup] = None) -> "Message":
        return await self.app.edit_message_text(self, text, inline_markup)
