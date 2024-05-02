import swibots
from enum import Enum
from swibots.base import SwitchObject
from typing import Literal

ADS_OPTIONS = ["VIDEO_1", "VIDEO_2"]


class ADInfo(SwitchObject):
    def __init__(
        self,
        app: "swibots.Client" = None,
        access_id: str = None,
        admin_id: str = None,
        app_id: str = None,
        id: str = None,
        type: Literal["VIDEO_1", "VIDEO_2", "IMAGE"] = None,
        **kwargs
    ):
        super().__init__(app, **kwargs)
        self.type = type
        self.app_id = app_id
        self.id = id
        self.admin_id = admin_id
        self.access_id = access_id

    def to_json(self):
        return {
            "id": self.id,
            "appId": self.app_id,
            "adminId": self.admin_id,
            "addAccessId": self.access_id,
            "type": self.type,
        }
