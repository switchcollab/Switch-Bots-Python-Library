from .get_channel import GetChannel
from .get_community import GetCommunity
from .get_group import GetGroup
from .permission import PermissionMethods
from .roles import RoleMethods
from .rolemember import RoleMemberMethods
from .ban_user import BanUser
from .unban_user import UnbanUser
from .create_channel import CreateChannel
from .update_channel import UpdateChannel
from .restrict_user import RestrictUser
from .get_community_member import GetCommunityMember
from .deduct_xp import DeductXP

class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetCommunityMember,
    GetGroup,
    RoleMethods,
    PermissionMethods,
    RoleMemberMethods,
    BanUser,
    UnbanUser,
    CreateChannel,
    UpdateChannel,
    RestrictUser,
    DeductXP
):
    pass
