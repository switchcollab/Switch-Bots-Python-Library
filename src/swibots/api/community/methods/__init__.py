from .get_channel import GetChannel
from .get_community import GetCommunity
from .get_group import GetGroup
from .roles import RoleMethods

class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetGroup,
    RoleMethods
):
    pass
