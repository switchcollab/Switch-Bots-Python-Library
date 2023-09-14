from typing import List, Optional
import swibots
from swibots.base import SwitchObject
from swibots.api.common import User
from swibots.api.community import Community, Channel, Group
from .inline_query_answer import InlineQueryAnswer

from swibots.utils.types import JSONDict


class InlineQuery(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        user_id: int = None,
        user: "User" = None,
        # receiver_id: int = None,
        # receiver: "User" = None,
        community_id: int = None,
        community: "Community" = None,
        group_id: int = None,
        group: "Group" = None,
        channel_id: int = None,
        channel: "Channel" = None,
        query_id: Optional[str] = None,
        offset: Optional[str] = None,
        query: Optional[str] = None,
    ):
        super().__init__(app)
        self.user_id = user_id
        self.user = user
        # self.receiver_id = receiver_id
        # self.receiver = receiver
        self.community_id = community_id
        self.community = community
        self.group_id = group_id
        self.group = group
        self.channel_id = channel_id
        self.channel = channel
        self.query_id = query_id
        self.offset = offset
        self.query = query

    def to_json(self) -> JSONDict:
        return {
            "text": self.text,
            "url": self.url,
            "callbackData": self.callback_data,
        }

    def from_json(self, data: JSONDict) -> "InlineQuery":
        if data is not None:
            self.user_id = data.get("userId")
            self.user = User.build_from_json(data.get("user"), self.app)
            # self.receiver_id = data.get("receiverId")
            # self.receiver = User.build_from_json(
            #     data.get("receiver"), self.app)
            self.community_id = data.get("communityId")
            self.community = Community.build_from_json(data.get("community"), self.app)
            self.group_id = data.get("groupId")
            self.group = Group.build_from_json(data.get("group"), self.app)
            self.channel_id = data.get("channelId")
            self.channel = Channel.build_from_json(data.get("channel"), self.app)
            self.query_id = data.get("id")
            self.offset = data.get("offset")
            self.query = data.get("query")
        return self

    async def answer(self, response: "InlineQueryAnswer"):
        return await self.app.answer_inline_query(self, response)
