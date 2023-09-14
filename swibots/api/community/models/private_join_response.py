from typing import Optional
from swibots.api.common.models import User
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class PrivateJoinResponse(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
    ):
        super().__init__(app)
        self.channel_id = None
        self.community_id = None
        self.group_id = None
        self.members = []

    def from_json(self, data: JSONDict | None) -> "PrivateJoinResponse":
        if data:
            self.channel_id = data.get("channelId")
            self.community_id = data.get("communityId")
            self.group_id = data.get("groupId")
            self.members = [
                User.build_from_json(member, self.app) for member in data.get("members")
            ]
        return self
