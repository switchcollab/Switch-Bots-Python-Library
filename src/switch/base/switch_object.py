from typing import Generic, List, Optional, TypeVar
from switch.utils.types import JSONDict


T = TypeVar("T")


class SwitchObject(Generic[T]):
    @classmethod
    def from_json(cls, data: Optional[JSONDict]) -> Optional[T]:
        return cls(**data)

    @classmethod
    def from_json_list(cls, data: Optional[JSONDict]) -> List[T]:
        return [cls(**item) for item in data]

    def to_json_request(self) -> JSONDict:
        return self.to_json()

    def to_json(self) -> JSONDict:
        return self.__dict__

    def __repr__(self) -> str:
        return self.to_json().__repr__()
