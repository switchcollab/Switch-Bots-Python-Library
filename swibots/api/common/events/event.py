from typing import Optional
import swibots
from swibots.base.switch_object import SwitchObject

# from switch.api.community.models import Community, Group, Channel
# from switch.base.switch_object import SwitchObject
# from switch.types import EventType
# from switch.api.common.models.user import User
# from switch.utils.types import JSONDict


class Event(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        type: Optional["swibots.EventType"] = None,
        data: Optional[dict] = None,
        community_id: Optional[str] = None,
        community: Optional["swibots.Community"] = None,
        group_id: Optional[str] = None,
        group: Optional["swibots.Group"] = None,
        channel_id: Optional[str] = None,
        channel: Optional["swibots.Channel"] = None,
        action_by_id: Optional[int] = None,
        action_by: Optional["swibots.User"] = None,
    ):
        super().__init__(app)
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

    def from_json(self, data: swibots.JSONDict) -> "Event":
        if data is not None:
            details = data.get("details") or {}
            self.type = swibots.EventType(data.get("type"))
            self.action_by_id = int(data.get("actionById"))
            self.action_by = swibots.User.build_from_json(
                data.get("actionBy"), self.app
            )
            self.community_id = details.get("communityId")
            self.community = swibots.Community.build_from_json(
                details.get("community"), self.app
            )
            if not self.community_id and self.community:
                self.community_id = self.community.id
            self.group_id = details.get("groupId")
            self.group = swibots.Group.build_from_json(details.get("group"), self.app)
            self.channel_id = details.get("channelId")
            self.channel = swibots.Channel.build_from_json(
                details.get("channel"), self.app
            )
            self.data = details
        return self

    def to_json(self) -> swibots.JSONDict:
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
