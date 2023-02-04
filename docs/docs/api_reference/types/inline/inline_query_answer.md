# InlineQueryAnswer

`Class swibots.api.chat.models.inline.InlineQueryAnswer`

Represents a result of an inline query that was chosen by the user and sent to their chat partner.

## Properties
- `query_id` (`str`): Unique identifier for the answered query
- `user_id` (`int`): The ID of the user who sent the query
- `title` (`str`): Title of the result
- `results` (List[[InlineQueryResult](./inline_query_result)]): A list of results for the inline query
- `next_offset` (`str`): Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes.

