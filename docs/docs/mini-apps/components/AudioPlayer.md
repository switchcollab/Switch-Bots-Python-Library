### AudioPlayer

The `AudioPlayer` class represents a component for playing audio in a user interface.

#### Properties

- `title` (Required): The title of the audio track.
- `url` (Required): The URL of the audio file to be played.
- `subtitle` (Optional): The subtitle or additional information about the audio track.
- `thumb` (Optional): The thumbnail image associated with the audio track. It can be an instance of the `Image` class or a URL string.

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