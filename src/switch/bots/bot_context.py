from typing import TYPE_CHECKING, Generic, TypeVar


if TYPE_CHECKING:
    from switch.bots.events import Event
    from switch.bots.bot import Bot
    from switch import SwitchApp


EventType = TypeVar("EventType", bound="Event")


class BotContext(Generic[EventType]):
    def __init__(self, bot: "Bot", event: EventType, app: "SwitchApp"):
        self.event = event
        self.bot = bot
        self.app = app
