import enum


class EventType(enum.Enum):
    """Represents the type of a request."""

    MESSAGE = "message"
    COMMAND = "command"
    CALLBACK_QUERY = "callback_query"


VALID_COMMAND_REGEX = r"^[\da-z0-9_]{1,32}$"
COMMAND_PARSER_REGEX = r"^/([\da-zA-Z0-9_]{1,32})(?:\s+(.*))?$"
