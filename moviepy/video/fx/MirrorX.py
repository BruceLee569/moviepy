from dataclasses import dataclass
from typing import List, Union

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MirrorX(Effect):
    """Flips the clip horizontally (and its mask too, by default)."""

    apply_to: Union[List, str] = "mask"

    def apply(self, clip: Clip) -> Clip:
        return clip.image_transform(lambda img: img[:, ::-1], apply_to=self.apply_to)
