# send_message

Send a text message to a user, channel or group.

## Signature

`async def send_message(message: Message, media: MediaUploadRequest = None) -> Message:`

## Parameters

- `message` ([Message](../types/message)): The message to send
- `media` ([MediaUploadRequest](../types/media_upload_request) | [EmbeddedMedia](../types/embedded_media.md)): The media to send with the message
