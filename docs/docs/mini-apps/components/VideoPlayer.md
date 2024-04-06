# VideoPlayer

The `VideoPlayer` class represents a video player in a user interface.

#### Properties

- `url` (Required): The URL of the video.
- `title` (Optional): The title of the video.
- `subtitle` (Optional): The subtitle or additional information about the video.
- `full_screen` (Optional, bool): Whether to open in full page
- `badges` (Optional, List[[Badge](../components/Badge.md)]): List of badges to display in full screen mode.

#### Usage Example

```python
# Create a VideoPlayer instance:
video_player = VideoPlayer(
    url="https://example.com/video.mp4",
    title="Video Title",
    subtitle="Video Subtitle"
)
```