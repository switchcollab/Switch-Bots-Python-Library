from typing import Type, TypeVar, Optional, List
import swibots
from swibots.api.bot.models import GameInfo


class GameMethods:
    async def create_leaderboard(
        self: "swibots.ApiClient",
        user_id: str | int,
        score: int,
        level: str | int = None,
        community_id: str = None,
        bot_id: str | int = None,
    ) -> GameInfo:
        return await self.bots_service.games.create_leaderboard(
            user_id, score, level=level, community_id=community_id, bot_id=bot_id
        )

    async def update_leaderboard(
        self: "swibots.ApiClient",
        id: str,
        user_id: str | int,
        score: int,
        level: int | str = None,
        bot_id: str | int = None,
    ) -> GameInfo:
        return await self.bots_service.games.update_leaderboard(
            id, user_id, score, level=level, bot_id=bot_id
        )

    async def get_global_leaderboard(
        self: "swibots.ApiClient", bot_id: Optional[str | int] = None
    ) -> List[GameInfo]:
        return await self.bots_service.games.get_global_leaderboard(bot_id)

    async def get_community_leaderboard(
        self: "swibots.ApiClient", community_id: str, bot_id: Optional[int | str] = None
    ) -> List[GameInfo]:
        return await self.bots_service.games.get_community_leaderboard(
            community_id, bot_id
        )

    async def get_game_score(
        self: "swibots.ApiClient",
        user_id: str | int,
        community_id: Optional[str] = None,
        bot_id: Optional[str | int] = None,
    ) -> GameInfo:
        return await self.bots_service.games.get_game_score(
            user_id, bot_id=bot_id, community_id=community_id
        )
