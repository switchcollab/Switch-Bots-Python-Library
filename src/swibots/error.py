from typing import Tuple


def _lstrip_str(in_s: str, lstr: str) -> str:
    """
    Args:
        in_s (:obj:`str`): in string
        lstr (:obj:`str`): substr to strip from left side
    Returns:
        :obj:`str`: The stripped string.
    """
    if in_s.startswith(lstr):
        res = in_s[len(lstr):]
    else:
        res = in_s
    return res


class SwitchError(Exception):
    """
    Base class for Seitch errors.
    .. seealso:: :wiki:`Exceptions, Warnings and Logging <Exceptions%2C-Warnings-and-Logging>`
    """

    def __init__(self, message: str):
        super().__init__()

        msg = _lstrip_str(message, "Error: ")
        msg = _lstrip_str(msg, "[Error]: ")
        msg = _lstrip_str(msg, "Bad Request: ")
        if msg != message:
            # api_error - capitalize the msg...
            msg = msg.capitalize()
        self.message = msg

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.message}')"

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.message,)


class NetworkError(SwitchError):
    """Base class for exceptions due to networking errors.
    Examples:
        :any:`Raw API Bot <examples.rawapibot>`
    """


class CancelError(SwitchError):
    pass
