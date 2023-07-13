from .get_channel import GetChannel
from .get_community import GetCommunity
from .get_group import GetGroup
from .permission import PermissionMethods
from .roles import RoleMethods

class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetGroup,
    RoleMethods,
    PermissionMethods
):
    pass
