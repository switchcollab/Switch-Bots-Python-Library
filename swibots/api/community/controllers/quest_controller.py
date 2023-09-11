import logging
from typing import TYPE_CHECKING, Optional, List
from swibots.api.common.models import User
from swibots.api.community.models import Quest, QuestCategory
from swibots.responses import CommunityQuestResponse
from urllib.parse import urlencode

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/quest"


class QuestsController:
    def __init__(self, client: "CommunityClient"):
        self.client = client

    async def create_quest(self, quest: Quest):
        response = await self.client.post(BASE_PATH, data=quest.to_json())
        return self.client.build_object(Quest, response.data)

    async def update_quest(self, quest: Quest):
        response = await self.client.put(BASE_PATH, data=quest.to_json())
        return self.client.build_object(Quest, response.data)

    async def get_quest(self, quest_id: int):
        return self.client.build_object(
            Quest, (await self.client.get(f"{BASE_PATH}/{quest_id}")).data
        )

    async def submit_quest(self, quest_id: int, community_id: str, description: str):
        response = await self.client.post(
            f"{BASE_PATH}/submitQuest",
            data={
                "questId": quest_id,
                "communityId": community_id,
                "description": description,
            },
        )
        return response.data

    async def approve_quest(
        self, community_id: str, quest_id: int, winner_id: int
    ) -> Quest:
        response = await self.client.post(
            f"{BASE_PATH}/approveQuest",
            data={
                "communityId": community_id,
                "questId": quest_id,
                "winnerMemberId": winner_id,
            },
        )
        return self.client.build_object(Quest, response.data)

    async def delete_quest(self, quest_id: str) -> bool:
        response = await self.client.delete(f"{BASE_PATH}/{quest_id}")
        return response.data

    async def get_quest_participants(self, quest_id: int):
        response = await self.client.get(
            f"{BASE_PATH}/getParticipants", data={"questId": quest_id}
        )
        return self.client.build_object(User, response.data)

    async def get_quests_by_community(self, community_id: str):
        response = await self.client.get(BASE_PATH, data={"communityId": community_id})
        return self.client.build_object(CommunityQuestResponse, response.data)

    # region

    async def get_quest_categories(self, community_id: str) -> List[QuestCategory]:
        return self.client.build_list(
            QuestCategory,
            (
                await self.client.get(
                    f"{BASE_PATH}/categories", data={"communityId": community_id}
                )
            ).data,
        )

    async def get_quest_category(self, category_id: str) -> QuestCategory:
        return self.client.build_object(
            QuestCategory,
            (
                await self.client.get(
                    f"{BASE_PATH}/category", data={"categoryId": category_id}
                )
            ).data,
        )

    async def create_quest_category(
        self, category_name: str, category_id: Optional[str] = None
    ) -> QuestCategory:
        response = await self.client.post(
            f"{BASE_PATH}/category",
            data={
                "categoryName": category_name,
                "categoryId": category_id or category_name,
            },
        )
        return self.client.build_object(QuestCategory, response.data)

    async def delete_quest_category(self, category_id: str) -> bool:
        response = await self.client.delete(
            f"{BASE_PATH}/category",
            data={
                "categoryId": category_id,
            },
        )
        return response.data

    # endregion
