from .get_channel import GetChannel
from .get_community import GetCommunity
from .get_group import GetGroup


class CommunityMethods(
    GetChannel,
    GetCommunity,
    GetGroup,
):
    pass
