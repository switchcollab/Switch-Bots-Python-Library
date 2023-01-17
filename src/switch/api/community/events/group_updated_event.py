from typing import Optional
from .community_event import CommunityEvent
from switch.api.community.models.channel import Channel
from switch.api.community.models.community import Community
from switch.api.community.models.group import Group
from switch.api.common.models.user import User
from switch.types import EventType


class GroupUpdatedEvent(CommunityEvent["GroupUpdatedEvent"]):
    def __init__(
        self,
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
            type=EventType.GROUP_UPDATE,
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
