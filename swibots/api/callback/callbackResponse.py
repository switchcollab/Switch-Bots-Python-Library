from typing import Dict, Any
from swibots.base import SwitchObject

class CallbackResponse(SwitchObject):

    def __init__(self):
        self.search_query = None
        self.file_url = None
        self.file_name = None
        self.input_value = None
        self.parent_id = None

    def get(self, key: str):
        return self.to_json().get(key)

    def from_json(self, data: Dict[str, Any] | None) -> Any:
        if data is not None:
            self.search_query = data.get("searchQuery")
            self.file_url = data.get("fileResponse")
            self.file_name = data.get("fileName")
            self.parent_id = data.get("callbackQueryId")
            self.input_value = data.get("inputValue")
        return self

    def to_json(self) -> Dict[str, Any]:
        return {
            "searchQuery": self.search_query,
            "fileResponse": self.file_url,
            "fileName": self.file_name,
            "callbackQueryId": self.parent_id,
            "inputValue": self.input_value
        }
