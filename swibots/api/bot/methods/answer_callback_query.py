from typing import Type, TypeVar, Optional, List
import swibots
from swibots.api.callback import AppPage


class AnswerCallback:
    async def answer_callback_query(
        self: "swibots.ApiClient",
        query_id: str,
        text: Optional[str] = None,
        url: Optional[str] = None,
        show_alert: Optional[bool] = False,
        cache_time: Optional[int] = None,
    ) -> bool:
        """
        Answer Callback query from callback button

        Arguments:
        query_id: str - Callback query id
        text: str - text
        url: str
        show_alert: bool - whether to display popup
        cache_time: int - cache time
        """
        return await self.bots_service.bots.answer_callback_query(
            query_id, text=text, url=url, show_alert=show_alert, cache_time=cache_time
        )

    async def answer_ui_query(
        self: "swibots.ApiClient", query_id: str, callback: AppPage
    ) -> bool:
        """Answer UI Query

        Args:
            query_id (str): _description_
            callback (AppPage): Callback component.

        Returns:
            Bool: whether callback was sent or not
        """
        return await self.bots_service.bots.answer_ui_query(query_id, callback=callback)
