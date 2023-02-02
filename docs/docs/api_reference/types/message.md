# Message

`Class pybots.api.chat.models.User`

The `Message` class represents a message sent to a chat.

## Properties

- `id` (`int`): The message's id.
- `user_id` (`int`): The message's sender's id.
- `user` ([User](./user)): The message's sender.
- `receiver_id` (`int`): The message's receiver's id.
- `receiver` ([User](./user)): The message's receiver.
- `message` (`str`): The message's text.
- `sent_date` (`int`): The message's sent date.
- `status` (`int`): The message's status.
- `request_id` (`int`): The message's request id.
- `channel_chat` (`bool`): Whether the message is a channel chat.
- `channel_id` (`int`): The message's channel's id.
- `channel` ([Channel](./channel)): The message's channel.
- `community_id` (`int`): The message's community's id.
- `community` ([Community](./community)): The message's community.
- `edit` (`bool`): Whether the message is an edit.
- `flag` (`int`): The message's flag.
- `forward` (`bool`): Whether the message is a forward.
- `group_chat` (`bool`): Whether the message is a group chat.
- `group_id` (`int`): The message's group's id.
- `group` ([Group](./group)): The message's group.
- `information` (`str`): The message's information.
- `inline_markup` ([InlineMarkup](./inline_markup)): The message's inline markup.
- `is_read` (`bool`): Whether the message is read.
- `media_link` (`str`): The message's media link.
- `replied_message` (`str`): The message's replied message.
- `replied_to_id` (`int`): The message's replied to id.
- `replied_to` ([Message](./message)): The message's replied to.
- `replies` ([Message](./message)): The message's replies.
- `reply_count` (`int`): The message's reply count.
- `personal_chat` (`bool`): Whether the message is a personal chat.
- `pinned` (`bool`): Whether the message is pinned.
- `reactions` (`List[str]`): The message's reactions.


## Api Methods

Unlike other types, the `Message` class has a few api methods to make it easier to work with.

- > ***async send(self,  media: [MediaUploadRequest](./media_upload_request) = None) -> Message *** 

    Sends the message. If the message has an id, it will be edited instead.

    You can also add media.

- > ***async reply(self,  reply: Message, media: [MediaUploadRequest](./media_upload_request) = None) -> Message *** 

    Replies to the message with the given message.

    You can also add media.

- > ***async reply_text(self,  text: str, inline_markup: Optional[[InlineMarkup](./inline_markup)] = None,  media: MediaUploadRequest = None) -> Message ***
     
    Replies to the message with the given text.

    You can also add an inline markup and media.

- > ***async edit_text(self,  text: str, inline_markup: Optional[[InlineMarkup](./inline_markup)] = None) -> Message ***
         
    Edits the message's text.

    You can also add an inline markup.

- > ***async delete(self) -> None *** 

    Deletes the message.

- > ***async def download(self, file_name: str = None, in_memory: bool = False, block: bool = True, progress: Callable = None, progress_args: tuple = ()) -> Optional[Union[BinaryIO, bytes]]:***

    Downloads the message's media (Please refer to [Downloading media](/docs/api_reference/methods/download_media)).
