from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from switch.bots.request import Request


ReqType= TypeVar('ReqType', bound= 'Request')

class BotContext(Generic[ReqType]):
    def __init__(self, request: ReqType):
        self.request = request