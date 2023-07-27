from typing import Optional
from swibots.utils.types import JSONDict
from swibots.api.common.models import User
from swibots.base.switch_object import SwitchObject
import swibots


class RestrictedUser(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        restricted: Optional[bool] = None,
        user_id: Optional[int] = None,
        community_id: Optional[str] = None,
        restricted_till: Optional[int] = None,
        user: Optional[User] = None,
    ):
        super().__init__(app)
        self.restricted = restricted
        self.community_id = community_id
        self.user_id = user_id
        self.user = user
        self.restricted_till = restricted_till

    def to_json(self) -> JSONDict:
        return {
            "communityId": self.community_id,
            "restricted": self.restricted,
            "restrictedTillTimestamp": self.restricted_till,
            "userId": self.user_id,
            "userInfo": self.user.to_json() if self.user else None,
        }

    @classmethod
    def from_json(self, data: JSONDict | None) -> "BanInfo":
        if data is not None:
            self.restricted = data.get("restricted")
            self.community_id = data.get("communityId")
            self.restricted_till = data.get("restrictedTillTimestamp")
            self.user_id = data.get("userId")
            self.user = User.build_from_json(data.get("userInfo"), self.app)
        return self
