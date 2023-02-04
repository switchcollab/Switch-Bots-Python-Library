# edit_message_text

Edits the text of a message.

## Signature

`async def edit_message_text(message: int | Message, text: str, inline_markup: InlineMarkup = None) -> Message:`

## Parameters

- `message` (int | [Message](../types/message)): The ID of the message to edit or the message itself
- `text` (str): The new text of the message
- `inline_markup` ([InlineMarkup](../types/inline_markup)): The new inline markup of the message


:::tip
This method does the same thing as [edit_message](../methods/edit_message), but it only edits the text of the message.
:::

:::tip
This method does the same thing as the `edit_text` method of the [Message](../types/message) class.
:::