from swibots.utils.ws.asyncstomp import AsyncWsClient


class SwitchWSAsyncClient(AsyncWsClient):
    def __init__(self, url: str, token: str = None):
        super().__init__(url)
        self._token = token

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, value: str):
        self._token = value

    def _set_default_headers(self, headers):
        headers = super()._set_default_headers(headers)
        headers["Authorization"] = f"Bearer {self._token}"
        return headers
