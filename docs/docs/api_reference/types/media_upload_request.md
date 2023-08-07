# MediaUploadRequest

The `MediaUploadRequest` class is used to upload media to the server, it's used when you
want to save or update messages to the server.

## Parameters

- `path` (str): The path to the file to upload
- `file_name` (str): The name of the file to upload
- `mime_type` (str): The MIME type of the file to upload
- `caption` (str): The caption of the file to upload
- `description` (str): The description of the file to upload
- `thumbnail` (str): The file path to use as thumbnail
- `block` (bool): Whether to block the thread until the upload is complete
- `callback` (Callable): The callback to monitor the upload progress
- `upload_args` (dict): The arguments to pass to the upload function
