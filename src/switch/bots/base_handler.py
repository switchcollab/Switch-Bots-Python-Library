
from abc import ABC
from typing import TYPE_CHECKING, Generic, TypeVar
from switch.utils.types import HandlerCallback

if TYPE_CHECKING:
    from switch.bots.bot import Bot
    from switch.switch_app import SwitchApp


CtxType = TypeVar("CtxType")
ResType = TypeVar("ResType")

class BaseHandler(Generic[CtxType, ResType], ABC):
    def __init__(self, callback: HandlerCallback[CtxType, ResType], **kwargs):
        self.callback = callback

    async def should_handle(self, context: CtxType) -> bool:
        return True

    async def handle(self,
        application: 'SwitchApp',
        context: CtxType,) -> ResType:
       if await self.should_handle(context=context) and self.callback is not None:
           return await self.callback(context)