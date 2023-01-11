from switch.base import SwitchRestClient
from switch.config import APP_CONFIG


class CommunityClient(SwitchRestClient):
    def __init__(self, base_url: str = APP_CONFIG['COMMUNITY_SERVICE']['BASE_URL']):
        super().__init__(base_url)
        self._users = None
        self._authorization = None