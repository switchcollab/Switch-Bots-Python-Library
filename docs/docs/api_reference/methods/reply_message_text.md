# reply_message_text

Replies to a message with a text.

## Signature

`async def reply_message_text(message: int | Message, text: str, inline_markup: InlineMarkup = None, media: MediaUploadRequest = None) -> Message:`

## Parameters

- `message` (int | [Message](/docs/api_reference/types/message)): The ID of the message to reply to or the message itself
- `text` (str): The text of the message
- `inline_markup` ([InlineMarkup](/docs/api_reference/types/inline_markup)): The inline markup of the message
- `media` ([MediaUploadRequest](/docs/api_reference/types/media_upload_request)): The media to send with the message


:::tip
This method does the same thing as [reply_message](/docs/api_reference/methods/reply_message), but it only sets the text of the message.
:::

:::tip
This method does the same thing as the `reply_text` method of the [Message](/docs/api_reference/types/message) class.
:::