from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class Role(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[int] = 0,
        community_id: Optional[str] = "",
        colour: Optional[str] = "",
        name: Optional[str] = "",
        members_count: Optional[int] = 0,
    ):
        super().__init__(app)

        self.id = id
        self.name = name
        self.community_id = community_id
        self.colour = colour
        self.members_count = members_count

    def to_json(self) -> JSONDict:
        return {
            "roleId": self.id,
            "roleColour": self.colour,
            "roleName": self.name,
            "noOfMembers": self.members_count,
            "communityId": self.community_id,
        }

    def from_json(self, data: JSONDict) -> "Role":
        if data is not None:
            self.id = data.get("id")
            self.name = data.get("roleName")
            self.colour = data.get("roleColour")
            self.community_id = data.get("communityId")
            self.members_count = data.get("noOfMembers")
        return self