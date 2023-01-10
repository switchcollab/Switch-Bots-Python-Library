import json
from typing import Tuple

from switch.error import NetworkError
from switch.utils import RestClient
from switch.utils.types import JSONDict
from switch.base import RestResponse


class SwitchRestClient(RestClient):
    def __init__(self, base_url: str = None, token: str = None):
        super().__init__()
        self._auth_token = token
        self._base_url = base_url

    @property
    def token(self):
        return self._auth_token

    @token.setter
    def token(self, token: str):
        self._auth_token = token

    @property
    def base_url(self, url: str):
        self._base_url = url

    @base_url.setter
    def base_url(self, url: str):
        self._base_url = url

    async def get(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.get`."""
        return await self.do_request(url, "GET", data, headers)

    async def post(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.post`."""
        return await self.do_request(url, "POST", data, headers)

    async def put(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.put`."""
        return await self.do_request(url, "PUT", data, headers)

    async def delete(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.delete`."""
        return await self.do_request(url, "DELETE", data, headers)

    async def patch(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.patch`."""
        return await self.do_request(url, "PATCH", data, headers)

    async def head(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.head`."""
        return await self.do_request(url, "HEAD", data, headers)

    async def options(self, url: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        """See :meth:`BaseRequest.options`."""
        return await self.do_request(url, "OPTIONS", data, headers)

    def parse_response(self, response: Tuple[int, bytes]) -> RestResponse[JSONDict]:
        decoded_s = response[1].decode("utf-8", "replace")
        try:
            jsonObject = json.loads(decoded_s)
        except ValueError as exc:
            jsonObject = decoded_s

        response = RestResponse(jsonObject, response[0], {})
        if response.is_error:
            raise NetworkError(response.error_message)
        return response

    def prepare_request_data(self, data: dict) -> dict:
        return super().prepare_request_data(data)

    def prepare_request_headers(self, headers: dict) -> dict:
        headers = super().prepare_request_headers(headers)
        if self._auth_token is not None:
            headers['Authorization'] = f'Bearer {self._auth_token}'
        return headers

    async def do_request(self, path: str, method: str, data: dict = None, headers: dict = None) -> RestResponse[JSONDict]:
        data = self.prepare_request_data(data)
        headers = self.prepare_request_headers(headers)
        return self.parse_response(await RestClient.do_request(self, self._base_url + path, method, data, headers))
