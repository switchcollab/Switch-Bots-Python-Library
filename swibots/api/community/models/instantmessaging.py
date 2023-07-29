from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class InstantMessaging(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[str] = None,
        enabled: Optional[bool] = None,
        group_id: Optional[str] = None,
        community_id: Optional[str] = None,
        bot_id: Optional[int] = None,
    ):
        super().__init__(app)
        self.id = id
        self.enabled = enabled
        self.group_id = group_id
        self.community_id = community_id
        self.bot_id = bot_id

    def to_json(self) -> JSONDict:
        return {
            "enabled": self.enabled,
            "groupId": self.group_id,
            "communityId": self.community_id,
            "botId": self.bot_id,
            "id": self.id,
        }

    @classmethod
    def from_json(self, data: JSONDict | None) -> "InstantMessaging":
        if data is not None:
            self.enabled = data.get("enabled")
            self.group_id = data.get("groupId")
            self.community_id = data.get("communityId")
            self.bot_id = data.get("botId")
            self.id = data.get("id")
        return self
