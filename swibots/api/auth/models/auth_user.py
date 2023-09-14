from typing import Optional, List
from swibots.base.switch_object import SwitchObject
from swibots.utils.types import JSONDict


class AuthUser(SwitchObject):
    def __init__(
        self,
        id: Optional[int] = None,
        user_name: Optional[str] = None,
        name: Optional[str] = None,
        creator_name: Optional[str] = None,
        verify_email: Optional[bool] = None,
        privacy: Optional[str] = None,
        is_bot: Optional[bool] = None,
        bot_privacy: Optional[str] = None,
        profile_colour: Optional[str] = None,
        otp: Optional[str] = None,
        otp_expiry: Optional[str] = None,
        bio: Optional[str] = None,
        imageurl: Optional[str] = None,
        private_imageurl: Optional[str] = None,
        gender: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        medias: Optional[List[str]] = None,
        more_about_this: Optional[str] = None,
        active: Optional[bool] = None,
        parent_id: Optional[int] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        self.id = id
        self.user_name = user_name
        self.name = name
        self.creator_name = creator_name
        self.verify_email = verify_email
        self.privacy = privacy
        self.is_bot = is_bot
        self.bot_privacy = bot_privacy
        self.profile_colour = profile_colour
        self.otp = otp
        self.otp_expiry = otp_expiry
        self.bio = bio
        self.imageurl = imageurl
        self.private_imageurl = private_imageurl
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.medias = medias
        self.more_about_this = more_about_this
        self.active = active
        self.parent_id = parent_id
        self.created_at = created_at
        self.updated_at = updated_at

    def from_json(self, data: Optional[JSONDict]) -> "AuthUser":
        super().from_json(data)
        if data is not None:
            self.id = data.get("id")
            self.user_name = data.get("user_name")
            self.name = data.get("name")
            self.creator_name = data.get("creator_name")
            self.verify_email = data.get("verifyEmail")
            self.privacy = data.get("privacy")
            self.is_bot = data.get("is_bot")
            self.bot_privacy = data.get("bot_privacy")
            self.profile_colour = data.get("profile_colour")
            self.otp = data.get("otp")
            self.otp_expiry = data.get("otp_expiry")
            self.bio = data.get("bio")
            self.imageurl = data.get("imageurl")
            self.private_imageurl = data.get("private_imageurl")
            self.gender = data.get("gender")
            self.date_of_birth = data.get("date_of_birth")
            self.medias = []
            for _ in range(1, 6):
                if media := data.get(f"media{_}"):
                    self.medias.append(media)
            self.more_about_this = data.get("more_about_this")
            self.active = data.get("active")
            self.parent_id = data.get("parent_id")
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")

        return self

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "creator_name": self.creator_name,
            "verifyEmail": self.verify_email,
            "privacy": self.privacy,
            "is_bot": self.is_bot,
            "bot_privacy": self.bot_privacy,
            "profile_colour": self.profile_colour,
            "otp": self.otp,
            "otp_expiry": self.otp_expiry,
            "bio": self.bio,
            "imageurl": self.imageurl,
            "private_imageurl": self.private_imageurl,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "media1": self.media1,
            "media2": self.media2,
            "media3": self.media3,
            "media4": self.media4,
            "media5": self.media5,
            "more_about_this": self.more_about_this,
            "active": self.active,
            "parent_id": self.parent_id,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
