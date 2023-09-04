from .models import *
from .auth_client import AuthClient
from .methods.get_me import GetMe

class AuthMethods(
    GetMe
):
    ...