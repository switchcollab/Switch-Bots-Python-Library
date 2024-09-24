from typing import Type, TypeVar, Optional, List
import swibots
from swibots.api.callback import AppPage


class AnswerCallback:
    async def answer_callback_query(
        self: "swibots.ApiClient",
        query_id: str,
        text: Optional[str] = None,
        url: Optional[str] = None,
        message_id: Optional[int] = None,
        show_alert: Optional[bool] = False,
        cache_time: Optional[int] = None,
        app_session_id: Optional[str] = None,
    ) -> bool:
        """
        Answer Callback query from callback button

        Arguments:
        query_id: str - Callback query id
        message_id: int:  message id linked to the message
        text: str - text
        url: str
        show_alert: bool - whether to display popup
        cache_time: int - cache time
        """
        return await self.bots_service.bots.answer_callback_query(
            query_id,
            text=text,
            url=url,
            show_alert=show_alert,
            cache_time=cache_time,
            message_id=message_id,
            app_session_id=app_session_id,
        )

    async def answer_ui_query(
        self: "swibots.ApiClient",
        query_id: str,
        message_id: int,
        callback: AppPage,
        app_session_id: str,
    ) -> bool:
        """Answer UI Query

        Args:
            query_id (str): callback query id
            message_id (int): message id linked to button
            callback (AppPage): Callback component.

        Returns:
            Bool: whether callback was sent or not
        """
        return await self.bots_service.bots.answer_ui_query(
            query_id, message_id, callback=callback, app_session_id=app_session_id
        )
