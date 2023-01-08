from typing import List, Optional

from switch.utils.types import JSONDict


class Message:
    def __init__(self, receiverId: int, message:str=None,  **kwargs):
        self.__dict__.update(kwargs)
        self.receiverId = receiverId
        self.message = message

  