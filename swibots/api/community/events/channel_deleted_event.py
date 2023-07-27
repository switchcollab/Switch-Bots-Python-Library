from typing import Optional
import swibots
from .community_event import CommunityEvent
from swibots.api.community.models.channel import Channel
from swibots.api.community.models.community import Community
from swibots.api.community.models.group import Group
from swibots.api.common.models.user import User
from swibots.types import EventType


class ChannelDeletedEvent(CommunityEvent["ChannelDeletedEvent"]):
    def __init__(
        self,
        app: "swibots.App" = None,
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
            type=EventType.COMMUNITY_CHANNEL_DELETE,
            data=data,
            action_by=action_by,
            action_by_id=action_by_id,
            community=community,
            community_id=community_id,
            group=group,
            group_id=group_id,
            channel=channel,
            channel_id=channel_id,
            user=user,
            user_id=user_id,
        )
