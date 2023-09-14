import swibots

from typing import Optional, List

from swibots.responses import CommunityQuestResponse
from swibots.api.community.models import Quest, QuestCategory
from swibots.api.common.models import User


class QuestsMethods:
    """
    Methods for managing permissions in a community.

    Args:
        client (swibots.ApiClient): The API client.
    """

    async def create_quest(self: "swibots.ApiClient", quest: Quest) -> Quest:
        """Create a quest

        Args:
            quest (Quest): the reference to quest

        Returns:
            `Quest`: the resultant
        """
        return await self.community_service.quests.create_quest(quest)

    async def update_quest(self: "swibots.ApiClient", quest: Quest):
        """Update a quest

        Args:
            quest (Quest): the reference to quest

        Returns:
            `Quest`: the updated quest
        """
        return await self.community_service.quests.update_quest(quest=quest)

    async def get_quest(self: "swibots.ApiClient", quest_id: int) -> Quest:
        """Get quest by quest id

        Args:
            quest_id (int): Quest ID

        Returns:
            `Quest`: the resulting quest.
        """
        return await self.community_service.quests.get_quest(quest_id)

    async def submit_quest(
        self: "swibots.ApiClient", quest_id: int, community_id: str, description: str
    ):
        """Submit quest in the community

        Args:
            quest_id (int): Quest ID.
            community_id (str): Community ID.
            description (str): Description

        Returns:
            _type_: _description_
        """
        return await self.community_service.quests.submit_quest(
            quest_id=quest_id, community_id=community_id, description=description
        )

    async def approve_quest(
        self: "swibots.ApiClient", community_id: str, quest_id: int, winner_id: int
    ) -> Quest:
        """Select a winner for the quest.

        Args:
            community_id (str): Community ID
            quest_id (int): Quest ID.
            winner_id (int): User id of winner.

        Returns:
            Quest: the resulting quest
        """
        return await self.community_service.quests.approve_quest(
            community_id=community_id, quest_id=quest_id, winner_id=winner_id
        )

    async def delete_quest(self: "swibots.ApiClient", quest_id: str) -> bool:
        """Delete a quest by quest id

        Args:
            quest_id (str): Quest ID

        Returns:
            bool: whether quest was deleted or not
        """
        return await self.community_service.quests.delete_quest(quest_id=quest_id)

    async def get_quest_participants(
        self: "swibots.ApiClient", quest_id: int
    ) -> List[User]:
        """Get Participants of the quest by quest id.

        Args:
            quest_id (int): Quest ID

        Returns:
            List[User]
        """
        return await self.community_service.quests.get_quest_participants(
            quest_id=quest_id
        )

    async def get_quests_by_community(self: "swibots.ApiClient", community_id: str):
        """Get Quests by community id

        Args:
            community_id (str): _description_

        Returns:
            `CommunityQuestResponse`
        """
        return await self.community_service.quests.get_quests_by_community(
            community_id=community_id
        )

    async def get_quest_categories(
        self: "swibots.ApiClient", community_id: str
    ) -> List[QuestCategory]:
        """Get quests categories by community id.

        Args:
            community_id (str): Community ID.

        Returns:
            List[QuestCategory]: List of quest categories.
        """
        return await self.community_service.quests.get_quest_categories(
            community_id=community_id
        )

    async def get_quest_category(
        self: "swibots.ApiClient", category_id: str
    ) -> QuestCategory:
        """Get quest category by category id.

        Args:
            category_id (str): Category ID.

        Returns:
            QuestCategory
        """
        return await self.community_service.quests.get_quest_category(
            category_id=category_id
        )

    async def create_quest_category(
        self: "swibots.ApiClient", category_name: str, category_id: Optional[str] = None
    ) -> QuestCategory:
        """Create quest category

        Args:
            category_name (str): Category Name
            category_id (Optional[str], optional): Category ID. Defaults to `category_name`

        Returns:
            QuestCategory:
        """
        return await self.community_service.quests.create_quest_category(
            category_name=category_name, category_id=category_id
        )

    async def delete_quest_category(
        self: "swibots.ApiClient", category_id: str
    ) -> bool:
        """Delete Quest category by category ID.

        Args:
            category_id (str): Category ID

        Returns:
            bool: Whether category was deleted or not.
        """
        return await self.community_service.quests.delete_quest_category(
            category_id=category_id
        )
