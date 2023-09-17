from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject


class InstantMessaging(SwitchObject):
    def __init__(
        self,
        id: Optional[str] = None,
        community_id: Optional[str] = None,
        group_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        bot_id: Optional[int] = None,
        enabled: Optional[bool] = False,
    ):
        self.id = id
        self.community_id = community_id
        self.group_id = group_id
        self.channel_id = channel_id
        self.bot_id = bot_id
        self.enabled = enabled

    def from_json(self, data: JSONDict | None) -> "InstantMessaging":
        if data is not None:
            self.id = data.get("id")
            self.community_id = data.get("communityId")
            self.group_id = data.get("groupId")
            self.channel_id = data.get("channelId")
            self.bot_id = data.get("botId")
            self.enabled = data.get("enabled")
        return self
