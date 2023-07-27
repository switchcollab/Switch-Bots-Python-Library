from typing import Optional, Any
from swibots.base import SwitchObject
from swibots.api.common.models import User
from swibots.utils.types import JSONDict


class Tournament(SwitchObject):
    def __init__(
        self,
        id: Optional[str] = None,
        community_id: Optional[str] = None,
        creator: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        cover_img: Optional[str] = None,
        status: Optional[str] = None,
        start_time: Optional[Any] = None,
        end_time: Optional[Any] = None,
        prizes: Optional[Any] = None,
        link: Optional[Any] = None,
        xp: Optional[str] = None,
        shortlist_min_cap: Optional[str] = None,
        state: Optional[str] = None,
    ):
        self.id = id
        self.community_id = community_id
        self.creator = creator
        self.name = name
        self.description = description
        self.cover_img = cover_img
        self.start_time = start_time
        self.end_time = end_time
        self.link = link
        self.xp = xp
        self.prizes = prizes
        self.status = status
        self.shortlist_min_cap = shortlist_min_cap
        self.state = state

    def to_json(self) -> JSONDict:
        return {
            "id": self.id,
            "community_id": self.community_id,
            "creator": self.creator,
            "cover_img": self.cover_img,
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "state": self.state,
            "status": self.status,
            "shortlist_min_cap": self.shortlist_min_cap,
            "link": self.link,
            "prizes": self.prizes,
            "xp": self.xp,
        }
