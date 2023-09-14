from typing import Optional
from swibots.base import SwitchObject
from swibots.utils.types import JSONDict


class GameInfo(SwitchObject):
    def __init__(
        self,
        id: Optional[str] = None,
        channel_id: Optional[str] = None,
        community_id: Optional[str] = None,
        user_id: Optional[str | int] = None,
        group_id: Optional[str] = None,
        bot_id: Optional[int] = None,
        score: Optional[int] = None,
        level: Optional[int] = None,
    ):
        self.id = id
        self.channel_id = channel_id
        self.community_id = community_id
        self.user_id = user_id
        self.group_id = group_id
        self.bot_id = bot_id
        self.score = score
        self.level = level

    def from_json(self, data: JSONDict | None) -> "GameInfo":
        if data is not None:
            self.id = data.get("id")
            self.channel_id = data.get("channelId")
            self.community_id = data.get("communityId")
            self.group_id = data.get("groupId")
            self.user_id = data.get("userId")
            self.bot_id = data.get("botId")
            self.score = data.get("score")
            self.level = data.get("level")
        return self

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "channelId": self.channel_id,
            "groupId": self.group_id,
            "communityId": self.community_id,
            "botId": self.bot_id,
            "score": self.score,
            "userId": self.user_id,
            "level": self.level,
        }
