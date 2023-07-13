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

    @classmethod
    def from_json(self, data: JSONDict) -> "Role":
        if data is not None:
            self.id = data.get("id")
            self.name = data.get("roleName")
            self.colour = data.get("roleColour")
            self.community_id = data.get("communityId")
            self.members_count = data.get("noOfMembers")
        return self


class RolePermission(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[int] = None,
        add_members: Optional[bool] = None,
        add_roles: Optional[bool] = None,
        send_messages: Optional[bool] = None,
        ban_users: Optional[bool] = None,
        change_info: Optional[bool] = None,
        delete_messages: Optional[bool] = None,
        dm_permission: Optional[bool] = None,
        pin_messages: Optional[bool] = None,
        restrict_messaging: Optional[bool] = None,
        role_id: Optional[int] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        super().__init__(app)
        self.id = id
        self.add_members = add_members
        self.add_roles = add_roles
        self.send_messages = send_messages
        self.ban_users = ban_users
        self.change_info = change_info
        self.delete_messages = delete_messages
        self.dm_permission = dm_permission
        self.pin_messages = pin_messages
        self.restrict_messaging = restrict_messaging
        self.role_id = role_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "roleId": self.role_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "rolePermission": {
                "addNewMembers": self.add_members,
                "addNewRoles": self.add_roles,
                "allowedToSendMessageInChannels": self.send_messages,
                "banUsers": self.ban_users,
                "changeCommunityInfo": self.change_info,
                "deletePostsAndMessages": self.delete_messages,
                "hasDMPermission": self.delete_messages,
                "pinMessages": self.pin_messages,
                "restrictMessaging": self.restrict_messaging,
            },
        }
    
    @classmethod
    def from_json(self, data: JSONDict) -> "RolePermission":
        if data is not None:
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")

            if data.get("rolePermission"):
                data = data["rolePermission"]

            self.add_members = data.get("addNewMembers")
            self.send_messages = data.get("allowedToSendMessageInChannels")
            self.delete_messages = data.get("deletePostsAndMessages")
            self.pin_messages = data.get("pinMessages")
            self.change_info = data.get("changeCommunityInfo")
            self.add_roles = data.get("addNewRoles")
            self.ban_users = data.get("banUsers")
            self.dm_permission = data.get("hasDMPermission")
            self.restrict_messaging = data.get("restrictMessaging")
        return self
