# Getting higher upload speed

### Default Parameters
- By default, library doesn't use of concurrent upload or threading.
- For the fan of speed and large files, one can make use of the below guide to get higher speed.

:::info
Upload speed can be increased by using `part_size` and `task_count` parameter in any of the upload methods (`reply_media`, `send_media`).
:::

### Example
- The below example use `100MB as part_size` and `30 as task_count`.
- It will create 30 threads and each will upload 100MB, until the complete file gets uploaded!
```python
await client.send_media(
    user_id=76,
    document="path/to/file.ext",
    part_size=100*1024*1024,
    task_count=30
)
```

:::warning
This parameters should be used depending on the machine, where the task is being executed!
:::
