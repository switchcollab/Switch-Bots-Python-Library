from enum import Enum
from typing import Any, Dict


JSONDict = Dict[str, Any]

class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"