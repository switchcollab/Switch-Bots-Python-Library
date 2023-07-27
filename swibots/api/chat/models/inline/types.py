import enum


class InlineQueryResultType(enum.Enum):
    """Represents the type of a inline query result."""

    ARTICLE = "ARTICLE"
    PHOTO = "PHOTO"
    DOCUMENT = "DOCUMENT"
    VIDEO = "VIDEO"
