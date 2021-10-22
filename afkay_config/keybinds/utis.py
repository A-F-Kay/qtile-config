from typing import List

from libqtile.config import Key

from afkay_config.keybinds.const import directions_keys_info


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
