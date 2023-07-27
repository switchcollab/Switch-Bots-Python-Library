# import the standard JSON parser
import json
import logging
from typing import Optional, Tuple

# import the REST library
import httpx

from swibots.error import NetworkError, SwitchError
from swibots.utils.types import JSONDict

log = logging.getLogger(__name__)

DEFAULT_HEADERS = {"Accept": "application/json"}


class RestClient:
    def __init__(
        self,
        connection_pool_size: int = 100,
        proxy_url: str = None,
        read_timeout: Optional[float] = None,
        write_timeout: Optional[float] = None,
        connect_timeout: Optional[float] = None,
        pool_timeout: Optional[float] = 1.0,
    ):
        timeout = httpx.Timeout(
            connect=connect_timeout,
            read=read_timeout,
            write=write_timeout,
            pool=pool_timeout,
        )
        limits = httpx.Limits(
            max_connections=connection_pool_size,
            max_keepalive_connections=connection_pool_size,
        )
        self._client_kwargs = dict(
            timeout=timeout,
            proxies=proxy_url,
            limits=limits,
        )

        try:
            self._client = self._build_client()
        except ImportError as exc:
            if "httpx[socks]" not in str(exc):
                raise exc

            raise RuntimeError(
                "To use Socks5 proxies, PTB must be installed via `pip install "
                "python-telegram-bot[socks]`."
            ) from exc

    def _build_client(self) -> httpx.AsyncClient:
        # type: ignore[arg-type]
        return httpx.AsyncClient(**self._client_kwargs)

    def initialize(self) -> None:
        log.debug("Initializing HTTPXRequest")
        if self._client.is_closed:
            self._client = self._build_client()

    async def shutdown(self) -> None:
        """See :meth:`BaseRequest.shutdown`."""
        if self._client.is_closed:
            log.debug("This HTTPXRequest is already shut down. Returning.")
            return
        await self._client.aclose()

    async def get(self, url: str, data: dict = None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.get`."""
        return await self.do_request(url, "GET", data, headers=headers)

    async def post(self, url: str, data: dict = None, form_data=None, files=None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.post`."""
        return await self.do_request(url, "POST", data, form_data, files, headers)

    async def put(self, url: str, data: dict = None, form_data=None, files=None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.put`."""
        return await self.do_request(url, "PUT", data, form_data, files, headers)

    async def delete(self, url: str, data: dict = None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.delete`."""
        return await self.do_request(url, "DELETE", data, headers=headers)

    async def patch(self, url: str, data: dict = None, form_data=None, files=None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.patch`."""
        return await self.do_request(url, "PATCH", data, form_data, files, headers)

    async def head(self, url: str, data: dict = None, headers: dict = None) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.head`."""
        return await self.do_request(url, "HEAD", data, headers)

    async def options(
        self, url: str, data: dict = None, headers: dict = None
    ) -> Tuple[int, bytes]:
        """See :meth:`BaseRequest.options`."""
        return await self.do_request(url, "OPTIONS", data, headers)

    def prepare_request_data(self, data: dict) -> dict:
#        data = {**data} if data else {}
        return data

    def prepare_request_headers(self, headers: dict) -> dict:
        if headers is None:
            headers = {}
        reqHeaders = {**headers}
        return reqHeaders

    async def do_request(
        self, url: str, method: str, data: dict = None, form_data=None, files=None, headers: dict = None
    ) -> Tuple[int, bytes]:
        if self._client.is_closed:
            raise RuntimeError("This RestClient is not initialized!")
        try:
            data = self.prepare_request_data(data)
            req_headers = self.prepare_request_headers(headers)
            if form_data is not None:
                # reqHeaders["Content-Type"] = "multipart/form-data"
                # reqHeaders["Accept"] = "application/json"
                response = await self._client.request(method, url, data=form_data, files=files, headers=req_headers)
            else:
                response = await self._client.request(method, url, json=data, headers=req_headers)
        except httpx.HTTPError as err:
            # HTTPError must come last as its the base httpx exception class
            # TODO p4: do something smart here; for now just raise NetworkError
            raise NetworkError(f"httpx HTTPError: {err}") from err

        return response.status_code, response.content

    @staticmethod
    def parse_json_payload(payload: bytes) -> JSONDict:
        """Parse the JSON returned from Switch.
        Tip:
            By default, this method uses the standard library's :func:`json.loads` and
            ``errors="replace"`` in :meth:`bytes.decode`.
            You can override it to customize either of these behaviors.
        Args:
            payload (:obj:`bytes`): The UTF-8 encoded JSON payload as returned by Telegram.
        Returns:
            dict: A JSON parsed as Python dict with results.
        Raises:
            SwitchError: If loading the JSON data failed
        """
        decoded_s = payload.decode("utf-8", "replace")
        try:
            return json.loads(decoded_s)
        except ValueError as exc:
            raise SwitchError("Invalid server response") from exc
