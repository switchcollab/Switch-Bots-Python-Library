---
sidebar_position: 3
---

# Inline queries

Switch supports inline queries. This means that you can send a query to a bot and receive a list of results from it. This is useful for things like searching for a specific item in a database, or getting a list of results from an API.

## Inline query basics

Every time a user types `@botname` in a chat, the bot will receive an `inline_query` event. This event contains the query string and the context of where the user is using the inline query.

The bot can send a response to the user's inline query. This response is a list of results. Each result can be an article, a photo, a video or document.

Please refer to the [InlineQueryAnswer](/docs/api_reference/types/inline/inline_query_answer) class for more information about the available inline query result types.


## Inline query example

Here is an example of how to handle an inline query:

```python

import logging
import json
from typing import Tuple
from swibots import Client, BotContext, MessageEvent, Message, InlineQuery, InlineQueryEvent, RestClient, RestResponse, JSONDict, NetworkError, InlineQueryResultArticle, InputMessageContent

logging.basicConfig(level=logging.INFO)

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
                    thumb_height=48,
                )
            )
        await query.answer(results)
    else:
        await query.answer("There was an error while searching for results.")


app.run()
```