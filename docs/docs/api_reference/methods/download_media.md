# download_media

Download a media file from a message.

## Signature

```python
async def download_media(
  message: Message,
  file_name: str = DOWNLOAD_MEDIA,
  in_memory: bool = False,
  block: bool = True,
  progress: DownloadProgressCallback = None,
  progress_args: tuple = ()
) -> Optional[Union[BinaryIO, bytes]]:
```

## Parameters

- `message` ([Message](../types/message)): The message to download the media
  from
- `file_name` (str): The file name to save the media to. If `in_memory` is
  `True`, this parameter is ignored.
- `in_memory` (bool): Whether to download the media to memory or to a file.
  Defaults to `False`.
- `block` (bool): Whether to block the current thread until the download is
  complete. Defaults to `True`.
- `progress`
  ([DownloadProgressCallback](../functions.md#downloadprogresscallback)): A
  callback function that is called when the download progress changes. Defaults
  to `None`.
- `progress_args` (tuple): Additional arguments to pass to the `progress`
  callback function. Defaults to `()`.

## Example

```python
from swibots import (
    Client,
    Message,
    DownloadProgress,
)

TOKEN = "YOUR_TOKEN_HERE"

app = Client(
    TOKEN,
    "A cool bot with annotations and everything you could possibly want :)"
)


@app.on_message()
async def on_message(message: Message):
    # Download the media to a file
    await message.download_media("my_media.jpg")

    # Download the media to memory
    media = await message.download_media(in_memory=True)

    # Download the media to a file and print the download progress
    async def progress_callback(progress: DownloadProgress):
        print(f"Downloaded {progress.downloaded} of {progress.total} bytes")

    await message.download("my_media.jpg", progress=progress_callback)

    # Download the media to memory and print the download progress
    async def progress_callback(progress: DownloadProgress):
        print(f"Downloaded {progress.downloaded} of {progress.total} bytes")

    media = await message.download(in_memory=True, progress=progress_callback)

    # Download the media to a file and cancel the download
    client = await message.download("my_media.jpg", block=False)
    client.cancel()

    # Download the media to memory and cancel the download
    client = await message.download(in_memory=True, block=False)
    client.cancel()


app.run()
```
