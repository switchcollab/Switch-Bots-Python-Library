from typing import List, Optional
from .base.switch_object import SwitchObject
from .api.community.models import QuestCategory, Quest
from .utils.types import JSONDict


class CommunityQuestResponse(SwitchObject):
    def __init__(
        self, categories: List[QuestCategory] = None, quests: List[Quest] = None
    ):
        super().__init__()
        self.categories = categories
        self.quests = quests

    def from_json(self, data: JSONDict | None) -> "CommunityQuestResponse":
        if data is not None:
            self.quests = [
                QuestCategory.build_from_json(quest) for quest in data.get("quests")
            ]
            self.categories = [
                QuestCategory.build_from_json(category)
                for category in data.get("availableCategories")
            ]
        return self
