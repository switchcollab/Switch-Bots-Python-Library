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


class ChatEvent(Event):
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
        action_by_id: Optional[str] = None,
        action_by: Optional[User] = None,
        data: Optional[dict] = None,
        user_id: Optional[str] = None,
        user: Optional[User] = None,
        message: Optional[Message] = None,
        message_id: Optional[str] = None,
    ):
        super().__init__(
            app=app,
            type=type,
            data=data,
            action_by=action_by,
            action_by_id=action_by_id,
            channel=channel,
            channel_id=channel_id,
            group=group,
            group_id=group_id,
            community=community,
            community_id=community_id,
        )
        self.user_id = user_id
        self.user = user
        self.message = message
        self.message_id = message_id

    def to_json(self) -> JSONDict:
        d = super().to_json()

        d.update(
            {
                "userId": self.user_id,
                "user": self.user.to_json(),
            }
        )
        return d

    def from_json(self, data: JSONDict) -> "ChatEvent":
        if data is not None:
            super().from_json(data)
            details = data.get("details") or {}
            self.user_id = data.get("userId") or data.get("senderId")
            self.user = User.build_from_json(
                details.get("user") or details.get("sender"), self.app)
            self.message_id = data.get("messageId")
            self.message = Message.build_from_json(
                details.get("message"), self.app)
        return self
