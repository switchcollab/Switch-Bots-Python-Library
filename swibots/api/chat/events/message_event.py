from typing import Optional
import swibots
from swibots.api.common.events.event import Event
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.api.chat.models.message import Message
from swibots.types import EventType
from swibots.utils.types import JSONDict
from .chat_event import ChatEvent


class MessageEvent(ChatEvent):
    """Message event"""

    def __init__(
        self,
        app: "swibots.App" = None,
        type: Optional[EventType] = None,
        community_id: Optional[str] = None,
        community: Optional[Community] = None,
        group_id: Optional[str] = None,
        group: Optional[Group] = None,
        channel_id: Optional[str] = None,
        channel: Optional[Channel] = None,
        action_by_id: Optional[int] = None,
        action_by: Optional[User] = None,
        data: Optional[dict] = None,
        user_id: Optional[str] = None,
        user: Optional[User] = None,
        message: Optional[Message] = None,
        message_id: Optional[int] = None,
    ):
        super().__init__(
            app=app,
            type=type or EventType.MESSAGE,
            community_id=community_id,
            community=community,
            group_id=group_id,
            group=group,
            channel_id=channel_id,
            channel=channel,
            action_by_id=action_by_id,
            action_by=action_by,
            data=data,
            user_id=user_id,
            user=user,
        )
        self.message_id = message_id
        self.message = message

    def from_json(self, data: JSONDict) -> "MessageEvent":
        super().from_json(data)
        if self.data is not None:
            self.message_id = data.get("messageId") or 0
            self.message: Message = Message.build_from_json(
                self.data.get("message"), self.app
            )

            self.message.user = self.user
            self.message.community = self.community
            self.message.group = self.group
            self.message.channel = self.channel
            self.message.receiver_id = (
                self.message.receiver_id or self.data.get("receiverId") or 0
            )
            self.message.receiver = User.build_from_json(
                self.data.get("receiver") or {}, self.app
            )

        return self
