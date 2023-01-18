from typing import Optional
from switch.api.common.events.event import Event
from switch.api.community.models.channel import Channel
from switch.api.community.models.community import Community
from switch.api.community.models.group import Group
from switch.api.common.models.user import User
from switch.api.chat.models.message import Message
from switch.types import EventType
from switch.utils.types import JSONDict
from .command_event import CommandEvent


class CallbackQueryEvent(CommandEvent):
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
        callback_data: Optional[JSONDict] = None,
    ):
        super().__init__(
            type=type or EventType.CALLBACK_QUERY,
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
            command=command,
            params=params,
        )
        self.callback_data = callback_data

    def from_json(self, data: JSONDict) -> "CallbackQueryEvent":
        super().from_json(data)
        if data is not None:
            self.callback_data = self.data.get("callbackData")
        return self
