from typing import Optional, List
from swibots.utils.types import JSONDict
from swibots.base.switch_object import SwitchObject
import swibots


class Quest(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        category: Optional[str] = None,
        category_id: Optional[str] = None,
        category_name: Optional[str] = None,
        claimed: Optional[bool] = None,
        community_id: Optional[str] = None,
        created_by: Optional[int] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        internal: Optional[bool] = None,
        name: Optional[str] = None,
        quest: Optional[str] = None,
        winner_ids: List[int] = None,
        xp: List[int] = None,
    ):
        super().__init__(app)
        self.category = category
        self.category_id = category_id
        self.category_name = category_name
        self.claimed = claimed
        self.community_id = community_id
        self.created_by = created_by
        self.description = description
        self.enabled = enabled
        self.internal = internal
        self.name = name
        self.quest = quest
        self.winner_ids = winner_ids
        self.xp = xp

    def to_json(self) -> JSONDict:
        return {
            "communityId": self.community_id,
            "enabled": self.enabled,
            "internal": self.internal,
            "quest": self.quest,
            "claimed": self.claimed,
            "winnerIds": self.winner_ids,
            "description": self.description,
            "category": self.category,
            "categoryName": self.category_name,
            "categoryId": self.category_id,
            "xp": self.xp,
            "createdBy": self.created_by,
        }

    def from_json(self, data: JSONDict | None) -> "Quest":
        if data is not None:
            self.community_id = data.get("communityId")
            self.enabled = data.get("enabled")
            self.internal = data.get("internal")
            self.name = data.get("name")
            self.quest = data.get("quest")
            self.claimed = data.get("claimed")
            self.winner_ids = data.get("winnerIds")
            self.description = data.get("description")
            self.category = data.get("category")
            self.category_id = data.get("categoryId")
            self.category_name = data.get("categoryName")
            self.xp = data.get("xp")
            self.created_by = int(data.get("createdBy") or 0)
        return self


class QuestCategory(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        category_id: Optional[str] = None,
        category_name: Optional[str] = None,
        community_id: Optional[str] = None,
        created_at: Optional[int] = None,
        updated_at: Optional[int] = None,
    ):
        super().__init__(app)
        self.community_id = community_id
        self.category_name = category_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.category_id = category_id

    def from_json(self, data: JSONDict | None) -> "QuestCategory":
        if data is not None:
            self.category_id = data.get("categoryId")
            self.category_name = data.get("categoryName")
            self.community_id = data.get("communityId")
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")
        return self
