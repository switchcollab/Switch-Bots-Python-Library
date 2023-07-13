from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
from swibots.api.common.models import User
import swibots


class RoleMember(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[int] = None,
        member_id: Optional[int] = None,
        community_id: Optional[str] = None,
        role_id: Optional[int] = None,
        user_id: Optional[int] = None,
        user: Optional[User] = None,
    ):
        super().__init__(app)
        self.id = id
        self.community_id = community_id
        self.member_id = member_id
        self.role_id = role_id
        self.user_id = user_id
        self.user = user

    def to_json(self) -> JSONDict:
        return {
            "communityId": self.community_id,
            "id": self.id,
            "memberId": self.member_id,
            "roleId": self.role_id,
            "userId": self.user_id,
            "userInfo": self.user.to_json(),
        }

    @classmethod
    def from_json(self, data: JSONDict) -> "RoleMember":
        if data is not None:
            self.community_id = data.get("communityId")
            self.id = data.get("id")
            self.member_id = data.get("memberId")
            self.role_id = data.get("roleId")
            self.user_id = data.get("userId")
            self.user = User.build_from_json(data.get("userInfo"), self.app)
        return self
