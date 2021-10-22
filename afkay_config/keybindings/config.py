from typing import List

from libqtile.config import Key

from afkay_config.keybindings.utis import \
    make_app_bindings, \
    make_direction_bindings, \
    make_group_bindings

direction_bindings: List[Key] = make_direction_bindings()

group_bindings: List[Key] = make_group_bindings()

app_bindings: List[Key] = make_app_bindings()
