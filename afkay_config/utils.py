import os
import socket
from typing import List, Optional

from libqtile.config import Group

mod = "mod4"  # Win/Super key
terminal = "alacritty"  # Super cool terminal
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def make_colors(color: str, secondary_color: Optional[str] = None) -> List[str]:
    return [color, secondary_color if secondary_color else color]


def make_groups() -> List[Group]:
    group_names = ["CHAT", "DEV", "SYS", "WWW", "MUS", "VID"]

    return [Group(name) for name in group_names]
