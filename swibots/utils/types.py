from enum import Enum
from typing import Any, Callable, Collection, Coroutine, Dict, TypeVar, Union

from swibots.error import CancelError


class IOClient:
    def cancel(self) -> None:
        raise CancelError()


class DownloadProgress:
    def __init__(self, downloaded: int, total: int, url: str, client: IOClient, file_name: str):
        self.downloaded = downloaded
        self.total = total
        self.url = url
        self.client = client
        self.file_name = file_name
        self.started = False


class UploadProgress:
    def __init__(self, current: int, readed: int, url: str, client: IOClient, file_name: str, callback, callback_args):
        self.current = current
        self.readed = readed
        self.url = url
        self.client = client
        self.file_name = file_name
        self.started = False
        self.callback = callback
        self.callback_args = callback_args

    def update(self, current: int) -> None:
        self.current = current
        self.readed += current
        if self.callback:
            self.callback(self, *self.callback_args)


CtxType = TypeVar("CtxType")
ResType = TypeVar("ResType")
HandlerCallback = Callable[[CtxType], Coroutine[Any, Any, ResType]]
FilterCallback = Callable[[CtxType], Coroutine[Any, Any, bool]]
DownloadProgressCallback = Callable[[
    DownloadProgress], Coroutine[Any, Any, None]]
UploadProgressCallback = Callable[[
    DownloadProgress], Coroutine[Any, Any, None]]

RT = TypeVar("RT")
SCT = Union[RT, Collection[RT]]
"""Single instance or collection of instances."""

JSONDict = Dict[str, Any]


class ReadCallbackStream(object):
    """Wraps a file-like object in another, but also calls a user
    callback with the number of bytes read whenever its `read()` method
    is called. Used for tracking upload progress, for example for a
    progress bar in a UI application. Idea taken from ActiveState Code Recipe:
    http://code.activestate.com/recipes/578669-wrap-a-string-in-a-file-like-object-that-calls-a-u/
    """

    def __init__(self, file_like, callback):
        if isinstance(file_like, str):
            self.file_like = open(file_like, "rb")
        else:
            self.file_like = file_like
        self.callback = callback

    def __len__(self):
        raise NotImplementedError()

    def read(self, *args):
        chunk = self.file_like.read(*args)
        if len(chunk) > 0:
            self.callback(len(chunk))
        return chunk

    def close(self):
        if hasattr(self.file_like, "close"):
            self.file_like.close()

class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
