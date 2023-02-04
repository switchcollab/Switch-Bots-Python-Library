# Types - Functions

Swibots have a number of built-in functions that can be used in the code of your Swibot. These functions are available in the `swibot` module.


## DownloadProgressCallback

A callback function that is called when the download progress changes.

### Signature
`DownloadProgressCallback = Callable[[DownloadProgress], Coroutine[Any, Any, None]]`

### Parameters
- `progress` ([DownloadProgress](#downloadprogress)): The download progress


## DownloadProgress

The download progress.

### Properties
- `downloaded` (int): The number of bytes that have been downloaded
- `total` (int): The total number of bytes to download
- `url` (str): The URL of the file being downloaded
- `client` ([IOClient](#ioclient)): The client that is downloading the file
- `file_name` (str): The file name of the file being downloaded
- `stared` (bool): Whether the download has started


## UploadProgressCallback

A callback function that is called when the upload progress changes.

### Signature

`UploadProgressCallback = Callable[[UploadProgress], Coroutine[Any, Any, None]]`

### Parameters

- `progress` ([UploadProgress](#uploadprogress)): The upload progress

## UploadProgress

The upload progress.

### Properties

- `current` (int): The current chunk size (in bytes) being uploaded
- `readed` (int): The number of bytes that have been uploaded
- `url` (str): The URL of the file being uploaded
- `client` ([IOClient](#ioclient)): The client that is uploading the file
- `file_name` (str): The file name of the file being uploaded
- `started` (bool): Whether the upload has started
- `callback` ([UploadProgressCallback](#uploadprogresscallback)): The callback function that is called when the upload progress changes
- `callback_args` (tuple): Additional arguments to pass to the `callback` callback function

## IOClient

The client that is used to download files. This is a class with just one metod `cancel()`, which can be used to cancel the download / upload.

It is used as a property of the [DownloadProgress](#downloadprogress) and [UploadProgress](#uploadprogress) objects.