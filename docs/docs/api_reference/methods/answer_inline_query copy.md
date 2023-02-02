# delete_message

Deletes a message.

Usually you will call this method using the `delete` method of the message object itself.

## Signature

`async def delete_message(message: int | Message) -> bool`

## Parameters

- `message` (int | [Message](/docs/types/message)): The message to delete (either the message ID or the message object itself)