# InlineQueryResult

`Class swibots.api.chat.models.inline.InlineQueryResult`

Represents a single result of an inline query

There are currently 4 types of inline query results, which are described below.

- [InlineQueryResultArticle](#inline_query_result_article)
- [InlineQueryResultPhoto](#inline_query_result_photo)
- [InlineQueryResultVideo](#inline_query_result_video)
- [InlineQueryResultDocument](#inline_query_result_document)


## Common Properties

These properties are common to all types of inline query results:

- `type` (`InlineQueryResultType`): Type of the result (ARTICLE, PHOTO, VIDEO, DOCUMENT)
- `title` (`str`, Optional): Title of the result
- `description` (`str`, Optional): Short description of the result
- `thumb_url` (`str`, Optional): URL of the thumbnail for the result
- `thumb_width` (`int`, Optional): Thumbnail width
- `thumb_height` (`int`, Optional): Thumbnail height
- `input_message` ([InputMessageContent](./input_message_content), Optional): Content of the message to be sent
- `reply_markup` ([InlineMarkup](/docs/api_reference/types/inline_markup), Optional): Inline keyboard attached to the message


## InlineQueryResultArticle

`Class swibots.api.chat.models.inline.InlineQueryResultArticle`

Represents a link to an article or web page.

### Extra Properties

- `article_url` (`str`): URL of the result


## InlineQueryResultPhoto

`Class swibots.api.chat.models.inline.InlineQueryResultPhoto`

Represents a link to a photo (external or saved as media on switch).

### Extra Properties

- `photo_url` (`str`): URL of the photo
- `mime_type` (`str`, Optional): MIME type of the photo, defaults to `image/jpeg`
- `photo_width` (`int`, Optional): Width of the photo
- `photo_height` (`int`, Optional): Height of the photo
- `caption` (`str`, Optional): Caption of the photo to be sent, 0-200 characters


## InlineQueryResultVideo

`Class swibots.api.chat.models.inline.InlineQueryResultVideo`

Represents a link to a video (external or saved as media on switch).

### Extra Properties

- `video_url` (`str`): URL of the video
- `mime_type` (`str`, Optional): MIME type of the video, defaults to `video/mp4`
- `video_width` (`int`, Optional): Width of the video
- `video_height` (`int`, Optional): Height of the video
- `video_duration` (`int`, Optional): Duration of the video in seconds


## InlineQueryResultDocument

`Class swibots.api.chat.models.inline.InlineQueryResultDocument`

Represents a link to a file (external or saved as media on switch).

### Extra Properties

- `document_url` (`str`): URL of the file
- `mime_type` (`str`, Optional): MIME type of the file

