from .rest_client import RestClient
from .ws import *
from .types import *
from urllib.parse import urlparse


def isUrl(text):
    """Validate, if text is url."""
    parse = urlparse(text)
    return parse.netloc and parse.scheme
