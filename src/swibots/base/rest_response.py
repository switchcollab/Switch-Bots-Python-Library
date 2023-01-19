from typing import Generic, TypeVar
from http.client import responses

from swibots.utils.types import RequestMethod


T = TypeVar("T")


class RestResponse(Generic[T]):
    def __init__(self, data: T, status_code: int, headers: dict):
        self.data = data
        self.status_code = status_code
        self.headers = headers

    @property
    def is_error(self) -> bool:
        return self.status_code >= 400

    @property
    def error_message(self) -> str:
        err = (
            self.data if self.data is not None and self.data != "" else responses[self.status_code]
        )
        return f"Error {self.status_code}: {err}"
