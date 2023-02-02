import logging
import json
from typing import Tuple
from swibots import (BotApp, BotContext, MessageEvent, Message, InlineQuery,
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


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA1LCJpc19ib3QiOnRydWUsImFjdGl2ZSI6dHJ1ZSwiaWF0IjoxNjc0MTc2MTA5LCJleHAiOjE2NzUzODU3MDl9.9Za0MMW9rTLEyplDO9hAAgoT330Xl0DjvGb9xl2-Lo4"

app = BotApp(TOKEN, "This is an inline query bot").register_command([
    # RegisterCommand("json", "Prints the message json", True),
    # RegisterCommand("echo", "Echoes the message", True),
    # RegisterCommand("buttons", "Shows buttons", True),
    # RegisterCommand(["movie", "movies", "film", "films", "search"],
    #                 "Show info about movies", True),
])


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
                    thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png",
                    thumb_width=48,
                    thumb_height=48))
        await query.answer(results)
    else:
        await query.answer("There was an error while searching for results.")


app.run()
