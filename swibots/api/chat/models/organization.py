import swibots
from typing import List, Optional
from swibots.base import SwitchObject
from swibots.api.bot.models import BotCommand
from swibots.api.common.models import User
from swibots.utils.types import JSONDict


class Organization(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        community_ids: List[str] = None,
        thumbnail: str = None,
        created_by: int = None,
        description: str = None,
        email: str = None,
        follower: bool = None,
        followers: int = None,
        id: str = None,
        instagram: str = None,
        twitter: str = None,
        telegram: str = None,
        name: str = None,
        profile_pic: str = None,
        source_code_link: str = None,
        website: str = None,
        created_at: str = None,
        updated_at: str = None,
        **kwargs
    ):
        super().__init__(app)
        self.community_ids = community_ids
        self.profile_pic = profile_pic
        self.name = name
        self.telegram = telegram
        self.twitter = twitter
        self.id = id
        self.followers = followers
        self.thumbnail = thumbnail
        self.email = email
        self.description = description
        self.follower = follower
        self.created_by = created_by
        self.instagram = instagram
        self.source_code_link = source_code_link
        self.website = website
        self.updated_at = updated_at
        self.created_at = created_at

    def to_json(self) -> JSONDict:
        return {
            "communityIds": self.community_ids,
            "coverPic": self.thumbnail,
            "createdAt": self.created_at,
            "createdBy": self.created_by,
            "description": self.description,
            "email": self.email,
            "follower": self.follower,
            "followers": self.followers,
            "id": self.id,
            "instagram": self.instagram,
            "name": self.name,
            "profilePic": self.profile_pic,
            "sourceCodeLink": self.source_code_link,
            "telegram": self.source_code_link,
            "twitter": self.twitter,
            "updatedAt": self.updated_at,
            "websiteLink": self.website,
        }

    def from_json(self, data: JSONDict | None) -> "Organization":
        if data:
            self.id = data.get("id")
            self.twitter = data.get("twitter")
            self.telegram = data.get("telegram")
            self.thumbnail = data.get("coverPic")
            self.source_code_link = data.get("sourceCodeLink")
            self.community_ids = data.get("communityIds")
            self.profile_pic = data.get("profilePic")
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")
            self.description = data.get("description")
            self.name = data.get("name")
            self.website = data.get("websiteLink")
            self.created_by = int(data.get("createdBy", 0))
        return self

    async def apps(self) -> List["OrgApp"]:
        return await self.app.get_organization_apps(self.id)

    async def followers(self) -> List[User]:
        return await self.app.get_organization_followers(self.id)


class OrgApp(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        commands: List[BotCommand] = None,
        created_at: str = None,
        org_id: str = None,
        name: str = None,
        role: str = None,
        id: str = None,
        status: str = None,
        **kwargs
    ):
        super().__init__(app, **kwargs)
        self.commands = commands
        self.created_at = created_at
        self.id = id
        self.name = name
        self.org_id = org_id
        self.role = role
        self.status = status
 
    def from_json(self, data: JSONDict | None) -> "OrgApp":
        if data:
#            self.commands = BotCommand.build_from_json_list(data.get("commands"), self.app)
            self.org_id = data.get("orgId")
            self.name = data.get("name")
            self.status = data.get("status")
            self.role = data.get("role")
        return self
    
    def to_json(self) -> JSONDict:
        return {
            "status": self.status,
            "commands": self.commands,
            "name": self.name,
            "role": self.role,
            "orgId": self.org_id,
            "id": self.id
        }