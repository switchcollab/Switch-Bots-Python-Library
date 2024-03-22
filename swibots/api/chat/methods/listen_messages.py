from typing import Type, TypeVar, Union
import swibots, asyncio
from swibots.api.community import Channel, Group
from swibots.api.chat import Message
from swibots.api.common.models import User
from swibots.api.chat.events import MessageEvent


class ListenMessages:
    async def listen_messages(
        self: "swibots.ApiClient", chat_id: str, count: int = 1, timeout: int = 60
    ):
        messageBox = []

        async def _on_message(ctx: swibots.BotContext[MessageEvent]):
            msg = ctx.event.message
            if msg.chat_id == chat_id:
                messageBox.append(msg)

        async def getMessages():
            while not len(messageBox) == count:
                await asyncio.sleep(0)

        app = self.bots_service.app

        from swibots.bots.handlers.message_handler import MessageHandler

        handler = MessageHandler(_on_message)
        try:
            app.add_handler(handler)
            await asyncio.wait_for(getMessages(), timeout=timeout)
        except TimeoutError as er:
            raise er
        finally:
            app.remove_handler(handler)
            
        if count == 1:
            return messageBox[0]
        return messageBox
