from typing import Optional
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class Community(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        username: Optional[str] = None,
        profile_url: Optional[str] = None,
        cover_url: Optional[str] = None,
        is_public: Optional[bool] = None,
        is_free: Optional[bool] = None,
        created_by: Optional[str] = None,
        guidelines: Optional[str] = None,
        description: Optional[str] = None,
        verified: Optional[bool] = None,
        category: Optional[str] = None,
        owner_id: Optional[int] = None,
        type: Optional[str] = None,
        link: Optional[str] = None,
        icon: Optional[str] = None,
        members_count: Optional[int] = None,
        groups_count: Optional[int] = None,
        channels_count: Optional[int] = None,
    ):
        super().__init__(app)
        self.id = id
        self.name = name
        self.username = username
        self.profile_url = profile_url
        self.cover_url = cover_url
        self.is_public = is_public
        self.is_free = is_free
        self.created_by = created_by
        self.guidelines = guidelines
        self.description = description
        self.verified = verified
        self.category = category
        self.owner_id = owner_id
        self.type = type
        self.link = link
        self.icon = icon
        self.members_count = members_count
        self.groups_count = groups_count
        self.channels_count = channels_count

    def to_json(self) -> JSONDict:
        return {
            "communityId": self.id,
            "communityName": self.name,
            "communityUsername": self.username,
            "communityProfileUrl": self.profile_url,
            "communityCoverUrl": self.cover_url,
            "isPublic": self.is_public,
            "isFree": self.is_free,
            "createdBy": self.created_by,
            "communityGuidelines": self.guidelines,
            "communityDescription": self.description,
            "verified": self.verified,
            "communityCategory": self.category,
            "communityType": self.type,
            "link": self.link,
            "icon": self.icon,
            "createdBy": self.owner_id,
            "member": self.members_count,
            "numberOfGroups": self.groups_count,
            "numberOfChannels": self.channels_count,
        }

    def from_json(self, data: Optional[JSONDict]) -> Optional["Community"]:
        if data is not None:
            self.id = data.get("communityId")
            self.name = data.get("communityName")
            self.username = data.get("communityUsername")
            self.profile_url = data.get("communityProfileUrl")
            self.cover_url = data.get("communityCoverUrl")
            self.is_public = data.get("isPublic")
            self.is_free = data.get("isFree")
            self.created_by = data.get("createdBy")
            self.guidelines = data.get("communityGuidelines")
            self.description = data.get("communityDescription")
            self.verified = data.get("verified")
            self.category = data.get("communityCategory")
            self.type = data.get("communityType")
            self.members_count = data.get("member")
            self.groups_count = data.get("numberOfGroups")
            self.channels_count = data.get("numberOfChannels")
            self.owner_id = int(data.get("createdBy"))
            self.link = data.get("link")
            self.icon = data.get("icon")
        return self
