from typing import Generic, Optional, TypeVar
import swibots
from swibots.api.common.events.event import Event
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.types import EventType
from swibots.utils.types import JSONDict

T = TypeVar("T", bound="CommunityEvent")


class CommunityEvent(Event, Generic[T]):
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
    ):
        super().__init__(
            app=app,
            type=type,
            data=data,
            action_by=action_by,
            action_by_id=action_by_id,
            community=community,
            community_id=community_id,
            group=group,
            group_id=group_id,
            channel=channel,
            channel_id=channel_id,
        )
        self.user_id = user_id
        self.user = user

    def to_json(self) -> JSONDict:
        d = super().to_json()

        d.update(
            {
                "communityId": self.community_id,
                "community": self.community.to_json() if self.community else None,
                "groupId": self.group_id,
                "group": self.group.to_json() if self.group else None,
                "channelId": self.channel_id,
                "channel": self.channel.to_json() if self.channel else None,
                "userId": self.user_id,
                "user": self.user.to_json() if self.user else None,
            }
        )
        return d

    def from_json(self, data: JSONDict) -> T:
        if data is not None:
            super().from_json(data)
            details = data.get("details") or {}
            self.user_id = data.get("userId")
            self.user = User.build_from_json(details.get("user"), self.app)
        return self
