from .base_handler import BaseHandler
from .event_handler import EventHandler
from .command_handler import CommandHandler
from .message_handler import MessageHandler
from .callback_query_handler import CallbackQueryHandler
from .channel_created_handler import ChannelCreatedHandler
from .channel_deleted_handler import ChannelDeletedHandler
from .channel_updated_handler import ChannelUpdatedHandler
from .group_created_handler import GroupCreatedHandler
from .group_deleted_handler import GroupDeletedHandler
from .group_updated_handler import GroupUpdatedHandler
from .member_joined_handler import MemberJoinedHandler
from .member_left_handler import MemberLeftHandler
from .user_banned_handler import UserBannedHandler
from .community_updated_handler import CommunityUpdatedHandler
from .unknown_command_handler import UnknownCommandHandler
from .inline_query_handler import InlineQueryHandler


class Handlers(
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    UnknownCommandHandler,
    ChannelCreatedHandler,
    ChannelDeletedHandler,
    ChannelUpdatedHandler,
    GroupCreatedHandler,
    GroupDeletedHandler,
    GroupUpdatedHandler,
    MemberJoinedHandler,
    MemberLeftHandler,
    UserBannedHandler,
    CommunityUpdatedHandler,
    InlineQueryHandler,
):
    pass
