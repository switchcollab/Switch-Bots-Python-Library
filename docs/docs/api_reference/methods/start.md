# start

Starts the app and starts listening for updates.

## Example

```python
from swibots import Client

app = Client("TOKEN")

async def main():
    await app.start()
    ...  # Invoke API methods
    await app.stop()


app.run(main())
```
