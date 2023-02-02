# send_text

Send a text message to a user, channel or group.

## Signature

`async def reply_message_text(text: str, to: Optional[int | User] = None, channel: Optional[Channel | str] = None, group: Optional[Group | str] = None,  inline_markup: InlineMarkup = None, media: MediaUploadRequest = None) -> Message:`

## Parameters

- `text` (str): The text of the message
- `to` (Optional[int | [User](../types/user)]): The ID of the user to reply to or the user itself
- `channel` (Optional[[Channel](../types/channel) | str]): The channel to reply to
- `group` (Optional[[Group](../types/group) | str]): The group to reply to
- `inline_markup` ([InlineMarkup](../types/inline_markup)): The inline markup of the message
- `media` ([MediaUploadRequest](../types/media_upload_request)): The media to send with the message



:::tip
This method does the same thing as [send_message](../methods/send_message), but it only sets the text of the message.
:::
