import swibots
from typing import Optional, List, Any
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
from .usertournament import UserTournament
from enum import Enum


class UserStatus(Enum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"


class BotPrivacy(Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class User(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        id: Optional[int] = None,
        name: Optional[str] = None,
        bio: Optional[str] = None,
        username: Optional[str] = None,
        image_url: Optional[str] = None,
        active: Optional[bool] = None,
        cover_image: Optional[str] = None,
        deleted: Optional[bool] = None,
        role_info: Optional[str] = None,
        link: Optional[str] = None,
        admin: Optional[bool] = None,
        is_bot: Optional[bool] = None,
        is_app: Optional[bool] = None,
        app_callback: Optional[str] = None,
        is_game: Optional[bool] = None,
        is_friend: Optional[bool] = None,
        tournaments: Optional[List[Any]] = None,
        status: Optional[str] = None,
        privacy: Optional[BotPrivacy] = BotPrivacy.PUBLIC,
    ):
        super().__init__(app)
        self.id = id
        self.name = name
        self.bio = bio
        self.username = username
        self.image_url = image_url
        self.active = active
        self.deleted = deleted
        self.link = link
        self.is_app = is_app
        self.app_callback = app_callback
        self.role_info = role_info
        self.admin = admin
        self.cover_image = cover_image
        self.is_bot = is_bot
        self.is_friend = is_friend
        self.is_game = is_game
        self.tournaments = tournaments
        self.status = status
        self.privacy = privacy.value

    def to_json(self) -> JSONDict:
        return {
            "cover_image": self.cover_image,
            "bot_id": self.id,
            "name": self.name,
            "bio": self.bio,
            "link": self.link,
            "is_friend": self.is_friend,
            "user_name": self.username,
            "imageurl": self.image_url,
            "active": self.active,
            "deleted": self.deleted,
            "roleInfo": self.role_info,
            "admin": self.admin,
            "is_bot": self.is_bot,
            "is_game": self.is_game,
            "is_app": self.is_app,
            "app_callback": self.app_callback,
            "tournamentsParticipated": [x.to_json(x) for x in self.tournaments or []],
            "bot_privacy": self.privacy,
        }

    def from_json(self, data: Optional[JSONDict] = None) -> "User":

        if data is not None:
            self.id = int(data.get("id") or data.get("botId") or 0)
            self.name = data.get("name") or data.get("botName")
            self.bio = data.get("bio")
            self.is_friend = data.get("is_friend")
            self.is_game = data.get("is_game")
            self.link = data.get("link")
            self.username = data.get("user_name") or data.get("username")
            self.image_url = data.get("imageurl") or data.get("imageUrl")
            self.active = data.get("active")
            self.deleted = data.get("deleted")
            self.role_info = data.get("roleInfo")
            self.admin = data.get("admin")
            self.is_app = data.get("is_app")
            self.app_callback = data.get("app_callback")
            self.is_bot = data.get("is_bot") or data.get("bot")
            self.cover_image = data.get("cover_image")
            self.tournaments = UserTournament.build_from_json_list(
                data.get("tournamentsParticipated") or [], self.app
            )
            status = data.get("user_status", {}).get("status")
            if status:
                self.status = getattr(UserStatus, status, None)
            if privacy := data.get("bot_privacy"):
                self.privacy = getattr(BotPrivacy, privacy, None)
        return self
