# delete_messages

Delete messages.

Usually you will call this method using the `delete` method of the message object itself.

## Signature

`async def delete_messages(message_ids: List[int | Message]) -> bool`

## Parameters

- `message` (int | [Message](../types/message)): The message to delete (either the message ID or the message object itself)