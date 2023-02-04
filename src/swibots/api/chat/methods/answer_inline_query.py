from typing import Type, TypeVar
import swibots
from swibots.api.chat.models import InlineQueryAnswer, InlineQuery


class AnswerInlineQuery:
    async def answer_inline_query(self: "swibots.ApiClient", query: InlineQuery, answer: InlineQueryAnswer) -> bool:
        """Answer inline query

        Args:
            query (:obj:`InlineQuery`): Inline query to answer to
            answer (str | InlineQueryAnswer): Answer to inline query, it can be either a string or an InlineQueryAnswer object, if it's a string, it will be used as the text of the answer
        """
        return await self.chat_service.messages.answer_inline_query(query, answer)
