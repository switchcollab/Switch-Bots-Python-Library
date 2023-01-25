from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots

class Channel(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        community_id: Optional[str] = None,
        enabled_free: Optional[bool] = None,
        enabled_public: Optional[bool] = None,
        default_channel: Optional[bool] = None,
        is_public: Optional[bool] = None,
        created_by: Optional[str] = None,
        icon: Optional[str] = None,
        channel_logo_url: Optional[str] = None,
        allowed_content: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        super().__init__(app)
        self.id = id
        self.name = name
        self.community_id = community_id
        self.enabled_free = enabled_free
        self.enabled_public = enabled_public
        self.default_channel = default_channel
        self.is_public = is_public
        self.created_by = created_by
        self.icon = icon
        self.channel_logo_url = channel_logo_url
        self.allowed_content = allowed_content
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self) -> JSONDict:
        return {
            "channelId": self.id,
            "channelName": self.name,
            "communityId": self.community_id,
            "enabledFree": self.enabled_free,
            "enabledPublic": self.enabled_public,
            "defaultChannel": self.default_channel,
            "isPublic": self.is_public,
            "createdBy": self.created_by,
            "icon": self.icon,
            "channelLogoUrl": self.channel_logo_url,
            "allowedContent": self.allowed_content,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    def from_json(self, data: JSONDict) -> "Channel":
        if data is not None:
            self.id = data.get("channelId")
            self.name = data.get("channelName")
            self.community_id = data.get("communityId")
            self.enabled_free = data.get("enabledFree")
            self.enabled_public = data.get("enabledPublic")
            self.default_channel = data.get("defaultChannel")
            self.is_public = data.get("isPublic")
            self.created_by = data.get("createdBy")
            self.icon = data.get("icon")
            self.channel_logo_url = data.get("channelLogoUrl")
            self.allowed_content = data.get("allowedContent")
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")
        return self
