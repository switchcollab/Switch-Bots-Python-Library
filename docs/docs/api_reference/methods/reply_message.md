# reply_message

Replies to a message.

## Signature

`async def reply_message_text(message: int | Message, reply: Message, media: MediaUploadRequest = None) -> Message:`

## Parameters

- `message` (int | [Message](/docs/api_reference/types/message)): The ID of the message to reply to or the message itself
- `reply` ([Message](/docs/api_reference/types/message)): The message to reply with
- `inline_markup` ([InlineMarkup](/docs/api_reference/types/inline_markup)): The inline markup of the message
- `media` ([MediaUploadRequest](/docs/api_reference/types/media_upload_request)): The media to send with the message


:::tip
This method does the same thing as the `reply` method of the [Message](/docs/api_reference/types/message) class.
:::