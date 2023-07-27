from .on_message import OnMessage
from .on_callback_query import OnCallbackQuery
from .on_channel_created import OnChannelCreated
from .on_channel_deleted import OnChannelDeleted
from .on_channel_updated import OnChannelUpdated
from .on_command import OnCommand
from .on_community_updated import OnCommunityUpdated
from .on_group_created import OnGroupCreated
from .on_group_deleted import OnGroupDeleted
from .on_group_updated import OnGroupUpdated
from .on_member_joined import OnMemberJoined
from .on_member_left import OnMemberLeft
from .on_user_banned import OnUserBanned
from .on_unknown_command import OnUnknownCommand
from .on_inline_query import OnInlineQuery


class Decorators(
    OnMessage,
    OnCallbackQuery,
    OnChannelCreated,
    OnChannelDeleted,
    OnChannelUpdated,
    OnCommand,
    OnCommunityUpdated,
    OnGroupCreated,
    OnGroupDeleted,
    OnGroupUpdated,
    OnMemberJoined,
    OnMemberLeft,
    OnUserBanned,
    OnUnknownCommand,
    OnInlineQuery,
):
    pass
