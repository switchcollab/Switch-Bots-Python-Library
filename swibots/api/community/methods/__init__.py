from .group_methods import GroupMethods
from .permission import PermissionMethods
from .roles import RoleMethods
from .rolemember import RoleMemberMethods
from .ban_user import BanUser
from .unban_user import UnbanUser
from .channel_methods import ChannelMethods
from .community_methods import CommunityMethods
from .restrict_user import RestrictUser
from .deduct_xp import DeductXP
from .quest_methods import QuestsMethods


class CommunityMethods(
    CommunityMethods,
    GroupMethods,
    RoleMethods,
    PermissionMethods,
    RoleMemberMethods,
    BanUser,
    UnbanUser,
    ChannelMethods,
    RestrictUser,
    DeductXP,
    QuestsMethods,
):
    pass
