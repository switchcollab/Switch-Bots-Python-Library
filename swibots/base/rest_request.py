from typing import Generic, TypeVar

from swibots.utils.types import RequestMethod


T = TypeVar("T")


class RestRequest(Generic[T]):
    def __init__(
        self, path: str, method: RequestMethod = RequestMethod.GET, data=None, headers: dict = None
    ):
        self.method = method
        self.path = path
        self.data = data
        self.headers = headers
