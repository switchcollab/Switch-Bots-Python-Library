from typing import Any, List, Optional
import swibots
from swibots.base import SwitchObject

from swibots.utils.types import JSONDict, SCT
from .inline_query_result import InlineQueryResult


class InlineQueryAnswer(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        query_id: Optional[str] = None,
        user_id: int = None,
        title: Optional[str] = None,
        results: List["InlineQueryResult"] = None,
        next_offset: Optional[str] = None,
        cache_time: int = None,
        is_personal: bool = True,
        pm_text: Optional[str] = None,
        pm_parameter: Optional[str] = None,
    ):
        super().__init__(app)
        self.query_id = query_id
        self.user_id = user_id
        self.title = title
        self.results = results
        self.next_offset = next_offset
        self.cache_time = cache_time
        self.is_personal = is_personal
        self.pm_text = pm_text
        self.pm_parameter = pm_parameter

    def to_json(self) -> JSONDict:
        return {
            "queryId": self.query_id,
            "userId": self.user_id,
            "title": self.title,
            "results":   [self._result_json(result) for result in self.results or []],
            "nextOffset": self.next_offset,
            "cacheTime": self.cache_time,
            "isPersonal": self.is_personal,
            "pmText": self.pm_text,
            "pmParameter": self.pm_parameter,
        }

    def _result_json(self, result):
        if isinstance(result, dict):
            return result
        else:
            return result.to_json()

    def add_result(self, result: SCT[Any]) -> "InlineQueryAnswer":
        if not self.results:
            self.results = []

        if isinstance(result, List):
            self.results.extend(result)
        else:
            self.results.append(result)
