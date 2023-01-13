from typing import Generic, List, Optional, TypeVar
from switch.utils.types import JSONDict


T = TypeVar("T")


class SwitchObject(Generic[T]):
    @classmethod
    def build_from_json(cls, data: Optional[JSONDict] = None) -> Optional[T]:
        if data is None:
            return None
        return cls().from_json(data)

    @classmethod
    def build_from_json_list(cls, data: Optional[JSONDict]) -> List[T]:
        return [cls(**item) for item in data]

    def to_json_request(self) -> JSONDict:
        return self.to_json()

    def to_json(self) -> JSONDict:
        return self.__dict__

    def from_json(self, data: Optional[JSONDict]) -> T:
        for key, value in data.items():
            setattr(self, key, value)
        return self

    def __repr__(self) -> str:
        return self.to_json().__repr__()
