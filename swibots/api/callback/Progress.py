from swibots.utils.types import JSONDict
from .types import Component
from enum import Enum


class Size(Enum):
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


class ProgressStyle(Enum):
    LINEAR = "linear"
    CIRCULAR = "circular"


class Progress(Component):
    type = "progress_bar"

    def __init__(
        self,
        color: str = None,
        size: Size = Size.MEDIUM,
        radius: int = 2,
        progress: int = False,
        animation: bool = False,
        progress_style: ProgressStyle = ProgressStyle.LINEAR,
    ):
        self.color = color
        self.size = size
        self.radius = radius
        self.progress = progress
        self.animation = animation
        self.progress_style = progress_style

    def to_json(self):
        return {
            "type": self.type,
            "color": self.color,
            "radius": self.radius,
            "interdeterminate": self.animation,
            "progress": self.progress,
            "barSize": self.size.value,
            "progressBarType": self.progress_style.value,
        }


class ListTileProgress(Progress):
    def __init__(
        self, color: str = None, progress: str = None, animation: bool = False
    ):
        super().__init__(color, progress=progress, animation=animation)
