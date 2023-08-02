import json
import logging
from typing import TYPE_CHECKING, List, Optional
from swibots.api.bot.models import BotInfo, BotCommandInfo, GameInfo
from swibots.error import SwitchError
from swibots.utils.types import JSONDict

if TYPE_CHECKING:
    from swibots.api.bot import BotClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/bots/game"


class GameController:
    def __init__(self, client: "BotClient"):
        self.client = client

    async def create_leaderboard(
        self, user_id: str | int, score: str | int = 0, bot_id: str | int = None
    ) -> GameInfo:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.post(
            f"{BASE_PATH}/leaderboard",
            data={"botId": bot_id, "userId": user_id, "score": score},
        )
        return self.client.build_object(GameInfo, response.data)

    async def update_leaderboard(
        self,
        id: str,
        user_id: str | int,
        score: str | int = 0,
        bot_id: str | int = None,
    ) -> None:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.put(
            f"{BASE_PATH}/leaderboard",
            data={"botId": bot_id, "userId": user_id, "score": score, "id": id},
        )
        return self.client.build_object(GameInfo, response.data)

    async def get_global_leaderboard(
        self, bot_id: Optional[str | int] = None
    ) -> List[GameInfo]:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.get(
            f"{BASE_PATH}/leaderboard/global?botId={bot_id}"
        )
        return self.client.build_list(GameInfo, response.data)

    async def get_community_leaderboard(
        self, community_id: str, bot_id: Optional[int | str] = None
    ) -> List[GameInfo]:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.get(
            f"{BASE_PATH}/leaderboard/community?communityId={community_id}&botId={bot_id}"
        )
        return self.client.build_list(GameInfo, response.data)

    async def get_game_score(
        self, user_id: str | int, bot_id: Optional[str | int] = None
    ) -> GameInfo:
        if not bot_id:
            bot_id = self.client.user.id
        response = await self.client.get(
            f"{BASE_PATH}/score?botId={bot_id}&userId={user_id}"
        )
        return self.client.build_object(GameInfo, response.data)