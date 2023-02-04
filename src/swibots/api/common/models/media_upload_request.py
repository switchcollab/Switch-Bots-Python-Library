import mimetypes
from swibots.utils.types import IOClient, ReadCallbackStream, UploadProgress, UploadProgressCallback


class MediaUploadRequest:
    def __init__(self,
                 path: str,
                 file_name: str = None,
                 mime_type: str = None,
                 caption: str = None,
                 description: str = None,
                 block: bool = True,
                 callback: UploadProgressCallback = None,
                 upload_args: tuple = ()):
        self.path = path
        self.file_name = file_name
        self.mime_type = mime_type
        self.caption = caption
        self.description = description
        self.block = block
        self.callback = callback
        self.upload_args = upload_args

    def data_to_request(self):
        return {
            "uploadMediaRequest.caption": self.caption,
            "uploadMediaRequest.description": self.description
        }

    def file_to_request(self, url):
        dProgress = UploadProgress(
            current=0,
            readed=0,
            file_name=self.file_name,
            client=IOClient(),
            url=url,
            callback=self.callback,
            args=self.upload_args
        )
        file = open(self.path, "rb")
        reader = ReadCallbackStream(
            file, dProgress.update
        )
        mime = self.mime_type or mimetypes.guess_type(
            self.path)[0] or "application/octet-stream"
        return {
            "uploadMediaRequest.file": (self.file_name or self.path, reader, mime)
        }
