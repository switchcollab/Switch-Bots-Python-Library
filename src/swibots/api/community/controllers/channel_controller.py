
import logging
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from swibots.api.community import CommunityClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/community/channels"


class ChannelController:
    def __init__(self, client: "CommunityClient"):
        self.client = client
