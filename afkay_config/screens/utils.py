from libqtile import bar
from libqtile.config import Screen

from afkay_config.screens.const import SCREENS_COUNT
from afkay_config.widgets.utils import make_widgets


def make_screens():
    def make_screen():
        return Screen(
            top=bar.Bar(
                make_widgets(),
                24
            ),
        )

    return [make_screen() for _ in range(SCREENS_COUNT)]
