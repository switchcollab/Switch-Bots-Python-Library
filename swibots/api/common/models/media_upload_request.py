import mimetypes, os
from io import BytesIO
from logging import getLogger
from swibots.utils.types import (
    IOClient,
    ReadCallbackStream,
    UploadProgress,
    UploadProgressCallback,
)

logger = getLogger(__name__)


class MediaUploadRequest:
    def __init__(
        self,
        path: str | BytesIO,
        file_name: str = None,
        mime_type: str = None,
        caption: str = None,
        description: str = None,
        block: bool = True,
        callback: UploadProgressCallback = None,
        thumbnail: str = None,
        upload_args: tuple = (),
        reduce_thumbnail: bool = True
    ):
        self.path = path
        self.file_name = file_name
        self.mime_type = mime_type
        self.caption = caption
        self.description = description
        self.block = block
        self.thumbnail = thumbnail
        self.callback = callback
        self.upload_args = upload_args
        self._handle_thumb = reduce_thumbnail

    def data_to_request(self):
        return {
            "uploadMediaRequest.caption": self.caption,
            "uploadMediaRequest.description": self.description,
        }

    def data_to_params_request(self):
        return {
            "caption": self.caption,
            "description": self.description,
            "mimeType": self.get_mime_type(),
            "fileSize": os.path.getsize(self.path)
            if os.path.exists(self.path)
            else None
            #            "thumbnail":self.thumbnail
        }

    def get_mime_type(self):
        path = self.path.name if isinstance(self.path, BytesIO) else self.path
        return (
            self.mime_type
            or mimetypes.guess_type(path)[0]
            or "application/octet-stream"
        )
    
    def generate_thumbnail(self, path, radius: int = 5, resize: bool = False, quality: int = 80):
        if self._handle_thumb:
            try:
                from PIL import Image, ImageFilter

                img = Image.open(path)
                if resize:
                    img.thumbnail((img.width // 2, img.height // 2), Image.BILINEAR)
                img = img.filter(ImageFilter.GaussianBlur(radius))
                obj = BytesIO()
                obj.name = os.path.basename(path)
                img.save(obj, optimize=True, quality=quality)
                return obj
            except ImportError:
                logger.debug("Pillow is not installed, Install it to add blur filter to thumbnail!")
        return open(path, "rb")

    def file_to_request(self, url):
        d_progress = UploadProgress(
            current=0,
            readed=0,
            file_name=self.file_name,
            client=IOClient(),
            url=url,
            callback=self.callback,
            callback_args=self.upload_args,
        )
        reader = ReadCallbackStream(self.path, d_progress.update)
        path = self.path.name if isinstance(self.path, BytesIO) else self.path
        mime = self.get_mime_type()
        result = {"uploadMediaRequest.file": (self.file_name or path, reader, mime)}
        if self.thumbnail:
            if os.path.exists(self.thumbnail):
                thumb = self.generate_thumbnail(self.thumbnail)
                result["uploadMediaRequest.thumbnail"] = (
                    self.thumbnail,
                    thumb,
                    mimetypes.guess_type(self.thumbnail)[0],
                )
            else:
                logger.error(
                    f"provided thumbnail: {self.thumbnail} is not a valid path!"
                )
        return result
