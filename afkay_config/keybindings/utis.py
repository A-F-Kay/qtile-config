from typing import List

from libqtile.config import Key
from libqtile.lazy import lazy

from afkay_config.const import groups, mod
from afkay_config.keybindings.const import directions_keys_info


def make_direction_bindings() -> List[Key]:
    bindings: List[Key] = []

    for key_info in directions_keys_info:
        for key_name in key_info.keys:
            for cb_info in key_info.callbacks:
                bindings.append(
                    Key(cb_info.key_hold,
                        key_name,
                        cb_info.cb(),
                        desc=cb_info.desc)
                )

    return bindings


def make_group_bindings() -> List[Key]:
    bindings: List[Key] = []

    for idx, group in enumerate(groups):
        group_key = str(idx + 1)

        bindings.append(Key([mod],
                            group_key,
                            lazy.group[group.name].toscreen(),
                            desc=f"Switch to group {group.name}")
                        )
        bindings.append(Key([mod, "shift"],
                            group_key,
                            lazy.window.togroup(
                                group.name,
                                switch_group=True
                            ),
                            desc=f"Switch to & move focused window "
                                 f"to group {group.name}"))

    return bindings
