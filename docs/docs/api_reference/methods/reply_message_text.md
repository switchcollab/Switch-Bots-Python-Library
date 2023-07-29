# reply_message_text

Replies to a message with a text.

## Signature

`async def reply_message_text(message: int | Message, text: str, inline_markup: InlineMarkup = None, media: MediaUploadRequest | EmbeddedMedia = None) -> Message:`

## Parameters

- `message` (int | [Message](../types/message)): The ID of the message to reply to or the message itself
- `text` (str): The text of the message
- `inline_markup` ([InlineMarkup](../types/inline_markup)): The inline markup of the message
- `media` ([MediaUploadRequest](../types/media_upload_request) | [EmbeddedMedia](../types/embedded_media.md)): The media to send with the message
- `cached_media` ([CachedMedia](../types/media)): The cached media to send with the message (media that has already been uploaded to the server)


:::tip
This method does the same thing as [reply_message](../methods/reply_message), but it only sets the text of the message.
:::

:::tip
This method does the same thing as the `reply_text` method of the [Message](../types/message) class.
:::