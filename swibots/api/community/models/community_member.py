from typing import Optional, List
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
from swibots.api.common.models import User
import swibots


class CommunityMember(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        admin: Optional[bool] = False,
        community_id: Optional[str] = None,
        enable_notification: Optional[bool] = None,
        id: Optional[int] = None,
        mute_channels: Optional[List[str]] = None,
        mute_groups: Optional[List[str]] = None,
        mute_notification: Optional[bool] = None,
        mute_period: Optional[str] = None,
        role_info: Optional[dict] = None,
        user_id: Optional[str] = None,
        user: Optional[User] = None,
        username: Optional[str] = None,
        xp: Optional[int] = None,
        xp_spend: Optional[int] = None,
    ):
        super().__init__(app)

        self.admin = admin
        self.id = id
        self.enable_notification = enable_notification
        self.mute_notification = mute_notification
        self.community_id = community_id
        self.user_id = user_id
        self.mute_groups = mute_groups
        self.mute_channels = mute_channels
        self.mute_period = mute_period
        self.role_info = role_info
        self.user = user
        self.username = username
        self.xp = xp
        self.xp_spend = xp_spend

    def to_json(self) -> JSONDict:
        return {
            "admin": self.admin,
            "communityId": self.community_id,
            "enableNotificationOnMentionAndPin": self.enable_notification,
            "id": self.id,
            "muteChannels": self.mute_channels,
            "muteGroups": self.mute_groups,
            "muteNotification": self.mute_notification,
            "mutePeriod": self.mute_period,
            "roleInfo": self.role_info,
            "userId": self.user_id,
            "userInfo": self.user.to_json() if self.user else None,
            "userName": self.username,
            "xp": self.xp,
            "xpSpend": self.xp_spend,
        }

    @classmethod
    def from_json(self, data: JSONDict | None) -> "CommunityMember":
        if data is not None:
            self.admin = data.get("admin")
            self.community_id = data.get("communityId")
            self.enable_notification = data.get("enableNotificationOnMentionAndPin")
            self.id = data.get("id")
            self.mute_channels = data.get("muteChannels")
            self.mute_groups = data.get("muteGroups")
            self.mute_notification = data.get("muteNotification")
            self.mute_period = data.get("mutePeriod")
            self.role_info = data.get("roleInfo")
            self.user_id = data.get("userId")
            self.username = data.get("userName")
            self.user = User.build_from_json(data.get("userInfo"), self.app)
            self.xp = data.get("xp")
            self.xp_spend = data.get("xp_spend")
        return self
