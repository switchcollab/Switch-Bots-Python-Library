from typing import Optional
from pyswitch.api.common.events.event import Event
from pyswitch.api.community.models.channel import Channel
from pyswitch.api.community.models.community import Community
from pyswitch.api.community.models.group import Group
from pyswitch.api.common.models.user import User
from pyswitch.api.chat.models.message import Message
from pyswitch.types import EventType
from pyswitch.utils.types import JSONDict
from .message_event import MessageEvent


class CommandEvent(MessageEvent):
    """Message event"""

    def __init__(
        self,
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
        command: Optional[str] = None,
        params: Optional[str] = None,
    ):
        super().__init__(
            type=type or EventType.COMMAND,
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
            message=message,
        )
        self.command = command
        self.params = params

    def from_json(self, data: JSONDict) -> "CommandEvent":
        super().from_json(data)
        if self.data is not None:
            self.command = self.data.get("command")
            self.params = self.data.get("commandParams")
        return self
