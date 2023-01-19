from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, Optional, TypeVar
from swibots.bots.filters.filter import Filter
from swibots.utils.types import HandlerCallback

if TYPE_CHECKING:
    from swibots.bots.bot import Bot
    from switch.switch_client import SwitchApp


CtxType = TypeVar("CtxType")
ResType = TypeVar("ResType")


class BaseHandler(Generic[CtxType, ResType], ABC):
    def __init__(
        self,
        callback: HandlerCallback[CtxType, ResType],
        filter: Optional[Filter] = None,
        **kwargs,
    ):
        self.callback = callback
        self.filter = filter

    async def on_app_start(self, app: "SwitchApp"):
        pass

    async def on_app_stop(self, app: "SwitchApp"):
        pass

    async def should_handle(self, context: CtxType) -> bool:
        return False

    async def handle(
        self,
        context: CtxType,
    ) -> ResType:
        if await self.should_handle(context=context) and self.callback is not None:
            return await self.callback(context)
