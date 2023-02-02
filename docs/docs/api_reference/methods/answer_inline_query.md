# answer_inline_query

This method sends an answer to an inline query. On success, True is returned.

## Signature

`async def answer_inline_query(query: InlineQuery, answer: InlineQueryAnswer) -> bool`

## Parameters

- `query` ([InlineQuery](../types/inline/inline_query)): The inline query to answer
- `answer` ([InlineQueryAnswer](../types/inline/inline_query_answer)): The answer to the inline query