import logging
from typing import TYPE_CHECKING
from swibots.api.community.models import Group

if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/groups"


class GroupController:
    def __init__(self, client: "CommunityClient"):
        self.client = client
