from .get_channel import GetChannel
from .get_community import GetCommunity
from .group_methods import GroupMethods
from .permission import PermissionMethods
from .roles import RoleMethods
from .rolemember import RoleMemberMethods
from .ban_user import BanUser
from .unban_user import UnbanUser
from .channel_methods import ChannelMethods
from .restrict_user import RestrictUser
from .get_community_member import GetCommunityMember
from .deduct_xp import DeductXP

class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetCommunityMember,
    GroupMethods,
    RoleMethods,
    PermissionMethods,
    RoleMemberMethods,
    BanUser,
    UnbanUser,
    ChannelMethods,
    RestrictUser,
    DeductXP
):
    pass
