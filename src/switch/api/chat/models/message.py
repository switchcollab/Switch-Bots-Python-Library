from typing import TYPE_CHECKING, List, Optional
from switch.base import SwitchObject

from switch.utils.types import JSONDict
from .inline_markup import InlineMarkup


class Message(SwitchObject):
    __slots__ = (
        "button_name",
        "button_pressed_id",
        "callback_data",
        "channel_chat",
        "channel_id",
        "command_name",
        "community_id",
        "edit",
        "flag",
        "forward",
        "group_chat",
        "group_id",
        "id",
        "information",
        "inline_markup",
        "is_read",
        "media_link",
        "mentioned_ids",
        "message",
        "personal_chat",
        "pinned",
        "reactions",
        "receiver_id",
        "replied_message",
        "replied_to",
        "replies",
        "reply_count",
        "request_id",
        "sent_date",
        "status",
        "user_id",
    )

    def __init__(
        self,
        id: int = None,
        user_id: int = None,
        receiver_id: int = None,
        message: str = None,
        sent_date: int = None,
        status: int = None,
        request_id: int = None,
        button_name: str = None,
        button_pressed_id: int = None,
        callback_data: str = None,
        channel_chat: bool = None,
        channel_id: int = None,
        command_name: str = None,
        community_id: int = None,
        edit: bool = None,
        flag: int = None,
        forward: bool = None,
        group_chat: bool = None,
        group_id: int = None,
        information: str = None,
        inline_markup: "InlineMarkup" = None,
        is_read: bool = None,
        media_link: str = None,
        mentioned_ids: List[int] = None,
        personal_chat: bool = None,
        pinned: bool = None,
        reactions: List[str] = None,
        replied_message: str = None,
        replied_to: int = None,
        replies: List["Message"] = None,
        reply_count: int = None,
        **kwargs,
    ):
        self.id = id
        self.user_id = user_id
        self.receiver_id = receiver_id
        self.message = message
        self.sent_date = sent_date
        self.status = status
        self.request_id = request_id
        self.button_name = button_name
        self.button_pressed_id = button_pressed_id
        self.callback_data = callback_data
        self.channel_chat = channel_chat
        self.channel_id = channel_id
        self.command_name = command_name
        self.community_id = community_id
        self.edit = edit
        self.flag = flag
        self.forward = forward
        self.group_chat = group_chat
        self.group_id = group_id
        self.information = information
        self.inline_markup = inline_markup
        self.is_read = is_read
        self.media_link = media_link
        self.mentioned_ids = mentioned_ids
        self.personal_chat = personal_chat
        self.pinned = pinned
        self.reactions = reactions
        self.replied_message = replied_message
        self.replied_to = replied_to
        self.replies = replies
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
            "inline_markup": self.inline_markup.to_json_request() if self.inline_markup else None,
            "isRead": self.is_read,
            "mediaLink": self.media_link,
            "mentionedIds": self.mentioned_ids,
            "message": self.message,
            "personalChat": self.personal_chat,
            "pinned": self.pinned,
            "reactions": self.reactions,
            "receiverId": self.receiver_id,
            "repliedMessage": self.replied_message,
            "repliedTo": self.replied_to,
            "replies": self.replies,
            "replyCount": self.reply_count,
            "requestId": self.request_id,
            "sentDate": self.sent_date,
            "status": self.status,
            "userId": self.user_id,
        }

    @classmethod
    def from_json(cls, data: Optional[JSONDict]) -> "Message":
        message = Message()
        if data is not None:
            message.button_name = data.get("buttonName")
            message.button_pressed_id = data.get("buttonPressedId")
            message.callback_data = data.get("callback_data")
            message.channel_chat = data.get("channelChat")
            message.channel_id = data.get("channelId")
            message.command_name = data.get("commandName")
            message.community_id = data.get("communityId")
            message.edit = data.get("edit")
            message.flag = data.get("flag")
            message.forward = data.get("forward")
            message.group_chat = data.get("groupChat")
            message.group_id = data.get("groupId")
            message.id = data.get("id")
            message.information = data.get("information")
            message.inline_markup = InlineMarkup.from_json(data.get("inline_markup"))
            message.is_read = data.get("isRead")
            message.media_link = data.get("mediaLink")
            message.mentioned_ids = data.get("mentionedIds")
            message.message = data.get("message")
            message.personal_chat = data.get("personalChat")
            message.pinned = data.get("pinned")
            message.reactions = data.get("reactions")
            message.receiver_id = data.get("receiverId")
            message.replied_message = data.get("repliedMessage")
            message.replied_to = data.get("repliedTo")
            message.replies = data.get("replies")
            message.reply_count = data.get("replyCount")
            message.request_id = data.get("requestId")
            message.sent_date = data.get("sentDate")
            message.status = data.get("status")
            message.user_id = data.get("userId")
        return message

    @classmethod
    def from_json_list(cls, data: Optional[JSONDict]) -> List["Message"]:
        return [cls.from_json(**item) for item in data]
