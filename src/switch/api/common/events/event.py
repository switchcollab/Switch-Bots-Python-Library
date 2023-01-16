from typing import Optional
from switch.api.community.models import Community, Group, Channel
from switch.base.switch_object import SwitchObject
from switch.types import EventType
from switch.api.common.models.user import User
from switch.utils.types import JSONDict


class Event(SwitchObject):
    def __init__(
        self,
        type: Optional[EventType] = None,
        data: Optional[dict] = None,
        community_id: Optional[str] = None,
        community: Optional[Community] = None,
        group_id: Optional[str] = None,
        group: Optional[Group] = None,
        channel_id: Optional[str] = None,
        channel: Optional[Channel] = None,
        action_by_id: Optional[str] = None,
        action_by: Optional[User] = None,
    ):
        self.type = type
        self.data = data
        self.action_by_id = action_by_id
        self.action_by = action_by
        self.community_id = community_id
        self.community = community
        self.group_id = group_id
        self.group = group
        self.channel_id = channel_id
        self.channel = channel

    def from_json(self, data: JSONDict) -> "Event":
        if data is not None:
            details = data.get("details") or {}
            self.type = EventType(data.get("type"))
            self.action_by_id = details.get("actionById")
            self.action_by = User.build_from_json(details.get("actionBy"))
            self.community_id = details.get("communityId")
            self.community = Community.build_from_json(details.get("community"))
            self.group_id = details.get("groupId")
            self.group = Group.build_from_json(details.get("group"))
            self.channel_id = details.get("channelId")
            self.channel = Channel.build_from_json(details.get("channel"))
            self.data = details
        return self

    def to_json(self) -> JSONDict:
        return {
            "type": self.type,
            "details": self.data,
            "communityId": self.community_id,
            "community": self.community.to_json() if self.community else None,
            "groupId": self.group_id,
            "group": self.group.to_json() if self.group else None,
            "channelId": self.channel_id,
            "channel": self.channel.to_json() if self.channel else None,
            "actionById": self.action_by_id,
            "actionBy": self.action_by.to_json() if self.action_by else None,
        }
