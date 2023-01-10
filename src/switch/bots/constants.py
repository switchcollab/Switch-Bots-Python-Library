import enum


class RequestType(enum.Enum):
    """Represents the type of a request."""
    MESSAGE = "message"
    CALLBACK_QUERY = "callback_query"