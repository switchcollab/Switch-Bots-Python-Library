from enum import Enum
from typing import Any, Callable, Collection, Coroutine, Dict, TypeVar, Union

CtxType = TypeVar("CtxType")
ResType = TypeVar("ResType")
HandlerCallback = Callable[[CtxType], Coroutine[Any, Any, ResType]]
FilterCallback = Callable[[CtxType], Coroutine[Any, Any, bool]]

RT = TypeVar("RT")
SCT = Union[RT, Collection[RT]]
"""Single instance or collection of instances."""

JSONDict = Dict[str, Any]


class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
