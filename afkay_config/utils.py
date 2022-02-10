from typing import List, Optional

from libqtile.config import Group


def make_colors(color: str, secondary_color: Optional[str] = None) -> List[str]:
    return [color, secondary_color if secondary_color else color]
