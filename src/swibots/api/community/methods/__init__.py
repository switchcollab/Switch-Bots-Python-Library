from .get_channel import GetChannel
from .get_community import GetCommunity
from .get_group import GetGroup
from .permission import PermissionMethods
from .roles import RoleMethods
from .rolemember import RoleMemberMethods

class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetGroup,
    RoleMethods,
    PermissionMethods,
    RoleMemberMethods
):
    pass
