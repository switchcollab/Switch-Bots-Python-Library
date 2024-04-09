### AudioPlayer

The `AudioPlayer` class represents a component for playing audio in a user interface.

#### Properties

- `id` (Optional): Any random id
- `title` (Required): The title of the audio track.
- `url` (Required): The URL of the audio file to be played.
- `subtitle` (Optional): The subtitle or additional information about the audio track.
- `thumb` (Optional): The thumbnail image associated with the audio track. It can be an `Image` class or URL string.
- `callback_data` (Optional, str): Detail about video player changes.
- `next_callback` (Optional): Callback for the next page.
- `previous_callback` (Optional): Callback for the previous page

#### Usage Example

```python
# Create an AudioPlayer instance:
audio_player = AudioPlayer(
    title="Example Audio Track",
    url="https://example.com/audio.mp3",
    subtitle="Artist: John Doe",
    thumb="https://example.com/thumbnail.jpg"
)
```