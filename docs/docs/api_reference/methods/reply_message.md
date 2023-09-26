# reply_message

Replies to a message.

## Signature

`async def reply_message_text(message: int | Message, reply: Message, embed_message:media: EmbeddedMedia = None) -> Message:`

## Parameters

- `message` (int | [Message](../types/message)): The ID of the message to reply to or the message itself
- `reply` ([Message](../types/message)): The message to reply with
- `inline_markup` ([InlineMarkup](../types/inline_markup)): The inline markup of the message
- `embedded_message` ([EmbeddedMedia](../types/embedded_media.md)): The media to send with the message


:::tip
This method does the same thing as the `reply` method of the [Message](../types/message) class.
:::