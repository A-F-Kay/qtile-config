from enum import Enum
from typing import Iterable, Callable, List, Dict

from libqtile.lazy import lazy
from pydantic import BaseModel

from afkay_config.const import mod


# ===================== Apps ===================== #
class AppInfo(BaseModel):
    name: str
    path: str


apps_keymap: Dict[str, AppInfo] = {
    'i': AppInfo(path="intellij-idea-ultimate-edition", name="Intellij IDEA"),
    'b': AppInfo(path="chromium", name="Chromium Browser"),
    't': AppInfo(path="telegram-desktop", name="Telegram messanging app"),
    'o': AppInfo(path="dvm run stable", name="Discord social app"),
    'v': AppInfo(path="tor-browser", name="Tor Browser"),
    'm': AppInfo(path="emacs", name="Doom emacs :evilsmile:"),
    'backslash': AppInfo(path="cool-retro-term", name="Nice retro terminal:)"),
}


# ================= Directions ================= #
class DirectionKeyName(Enum):
    UP = 'up'
    LEFT = 'left'
    DOWN = 'down'
    RIGHT = 'right'


class CallbackInfo(BaseModel):
    cb: Callable
    desc: str
    key_hold: List[str]


class DirectionKeyInfo:
    keys: List[str]
    callbacks: List[CallbackInfo]

    def __init__(self,
                 keys: List[str],
                 direction: DirectionKeyName,
                 move_focus: Callable,
                 move_window: Callable,
                 grow_window: Callable):
        self.keys = keys
        self.callbacks = [
            CallbackInfo(
                cb=move_focus,
                desc=f"Move focus to {direction}",
                key_hold=[mod]
            ),
            CallbackInfo(
                cb=move_window,
                desc=f"Move window {direction}",
                key_hold=[mod, "shift"]
            ),
            CallbackInfo(
                cb=grow_window,
                desc=f"Grow window to {direction}",
                key_hold=[mod, "control"]
            ),
        ]


# Assuming QWERTY / ЙЦУКЕН
directions_keys_info: Iterable[DirectionKeyInfo] = (
    DirectionKeyInfo(keys=['w'],
                     # keys=['w', 'ц'],
                     direction=DirectionKeyName.UP,
                     move_focus=lazy.layout.up,
                     move_window=lazy.layout.shuffle_up,
                     grow_window=lazy.layout.grow_up
                     ),
    DirectionKeyInfo(keys=['a'],
                     # keys=['a', 'ф'],
                     direction=DirectionKeyName.LEFT,
                     move_focus=lazy.layout.left,
                     move_window=lazy.layout.shuffle_left,
                     grow_window=lazy.layout.grow_left,
                     ),
    DirectionKeyInfo(keys=['s'],
                     # keys=['s', 'ы'],
                     direction=DirectionKeyName.DOWN,
                     move_focus=lazy.layout.down,
                     move_window=lazy.layout.shuffle_down,
                     grow_window=lazy.layout.grow_down,
                     ),
    DirectionKeyInfo(keys=['d'],
                     # keys=['d', 'в'],
                     direction=DirectionKeyName.RIGHT,
                     move_focus=lazy.layout.right,
                     move_window=lazy.layout.shuffle_right,
                     grow_window=lazy.layout.grow_right,
                     ),
)
