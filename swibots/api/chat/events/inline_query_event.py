from typing import Optional
import swibots
from swibots.api.common.events.event import Event
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.api.chat.models.message import Message
from swibots.api.chat.models.inline.inline_query import InlineQuery
from swibots.types import EventType
from swibots.utils.types import JSONDict
from .chat_event import ChatEvent


class InlineQueryEvent(ChatEvent):
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
        user_id: Optional[int] = None,
        user: Optional[User] = None,
        query: Optional[str] = None,
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
        self.query = query

    def from_json(self, data: JSONDict) -> "InlineQueryEvent":
        super().from_json(data)
        if self.data is not None:
            self.query = InlineQuery.build_from_json(
                self.data.get("inlineQuery"), self.app
            )
            self.user = self.action_by
            self.user_id = self.action_by_id

        self.query.user = self.user
        self.query.user_id = self.user_id

        return self
