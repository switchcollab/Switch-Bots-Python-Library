import swibots
from swibots.base import SwitchObject
from typing import List


class SessionUser(SwitchObject):
    def __init__(
        self,
        app: "swibots.Client" = None,
        session_id: str = None,
        user_id: int = None,
        name: str = None,
        username: str = None,
        image_url: str = None,
        role: str = None,
        **kwargs
    ):
        self.session_id = session_id
        self.user_id = user_id
        self.name = name
        self.username = username
        self.role = role
        self.image_url = image_url

    def from_json(self, data=None):
        if data is not None:
            self.session_id = data.get("id")
            self.name = data.get("name")
            self.username = data.get("username")
            self.role = data.get("role")
            self.image_url = data.get("imageUrl")
            self.user_id = data.get("userId")
        return self


class SessionInfo(SwitchObject):
    def __init__(
        self,
        app: "swibots.Client" = None,
        id: str = None,
        app_id: str = None,
        allow_members: bool = False,
        members: List[SessionUser] = None,
        chat_group_id: str = None,
        **kwargs
    ):
        self.id = id
        self.app_id = app_id
        self.allow_members = allow_members
        self.members = members
        self.chat_group_id = chat_group_id

    def from_json(self, data=None):
        if data is not None:
            self.id = data.get("id")
            self.app_id = data.get("appId")
            self.allow_members = data.get("canMemberControlScreen")
            self.members = [
                SessionUser().from_json(member) for member in data.get("members", [])
            ]
            self.chat_group_id = data.get("groupId")
        return self
