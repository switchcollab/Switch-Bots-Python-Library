from .delete_bot_info import DeleteBotInfo
from .get_bot_info import GetBotInfo
from .update_bot_info import UpdateBotInfo
from .game_methods import GameMethods

class BotMethods(
    DeleteBotInfo,
    GetBotInfo,
    UpdateBotInfo,
    GameMethods
):
    pass
