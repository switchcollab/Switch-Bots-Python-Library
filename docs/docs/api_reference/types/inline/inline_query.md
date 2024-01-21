# InlineQuery

`Class swibots.api.chat.models.inline.InlineQuery`

The InlineQuery object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

## Properties

- `id` (`str`): Unique identifier for this query
- `user_id` (`int`): The ID of the user who sent the query
- `user` ([User](../user)): The user who sent the query
- `community_id` (`int`): The ID of the community where the query was sent
- `community` ([Community](../community)): The community where the query was sent
- `group_id` (`int`): The ID of the group where the query was sent
- `group` ([Group](../group)): The group where the query was sent
- `channel_id` (`int`): The ID of the channel where the query was sent
- `channel` ([Channel](../channel)): The channel where the query was sent
- `query_id` (`str`): Unique identifier for this query
- `offset` (`str`): Offset of the results to be returned, can be controlled by the bot
- `query` (`str`): Text of the query (up to 256 characters)


## Methods

> ***answer(response: [InlineQueryAnswer](./inline_query_answer)]) -> bool:***
  Use this method to send answers to an inline query. On success, True is returned.
  No more than 50 results per query are allowed.

## Example

```python
import logging
import json
from typing import Tuple
from swibots import (Client, BotContext, MessageEvent, Message, InlineQuery,  
                     InlineQueryEvent, RestClient, RestResponse, JSONDict,
                     NetworkError, InlineQueryResultArticle,
                     InputMessageContent)

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

restclient = RestClient()


def parse_response(response: Tuple[int, bytes]) -> RestResponse[JSONDict]:
  decoded_s = response[1].decode("utf-8", "replace")
  try:
    jsonObject = json.loads(decoded_s)
  except ValueError as exc:
    jsonObject = decoded_s

  response = RestResponse(jsonObject, response[0], {})
  if response.is_error:
    raise NetworkError(response.error_message)
  return response


TOKEN = "your_token"

app = Client(TOKEN, "This is an inline query bot")

@app.on_message()
async def on_message(ctx: BotContext[MessageEvent]):
  message: Message = ctx.event.message
  log.info(f"Message: {message.message}")
  await message.reply_text(f"Echo: {message.message}")


@app.on_inline_query()
async def on_inline_query(ctx: BotContext[InlineQueryEvent]):
  query: InlineQuery = ctx.event.query
  log.info(f"Inline query: {query.query}")
  await query.answer(f"Searching results for {query.query}...")
  url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={query.query}&limit=50"
  response = parse_response(await restclient.get(url))
  if response.status_code == 200:
    data = response.data
    results = []
    for i in range(len(data[1])):
      results.append(
        InlineQueryResultArticle(
          id=str(i),
          title=data[1][i],
          description=data[1][i],
          input_message=InputMessageContent(data[2][i]),
          article_url=data[3][i],
          thumb_url=
          "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png",
          thumb_width=48,
          thumb_height=48))
    await query.answer(results)
  else:
    await query.answer("There was an error while searching for results.")


app.run()


```
