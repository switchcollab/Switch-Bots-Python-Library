from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


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
        can_deduct_xp: Optional[bool] = None,
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
        self.can_deduct_xp = can_deduct_xp
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
                "canDeductXPFromUser": self.can_deduct_xp,
                "restrictMessaging": self.restrict_messaging,
            },
        }

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
            self.can_deduct_xp = data.get("canDeductXPFromUser")
            self.ban_users = data.get("banUsers")
            self.dm_permission = data.get("hasDMPermission")
            self.restrict_messaging = data.get("restrictMessaging")
        return self
