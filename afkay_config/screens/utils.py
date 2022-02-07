from libqtile import bar
from libqtile.config import Screen

from afkay_config.screens.const import SCREENS_COUNT
from afkay_config.widgets.utils import make_widgets


def make_screens():
    def make_screen(screen: int):
        return Screen(
            top=bar.Bar(
                make_widgets(screen),
                24
            ),
        )

    return [make_screen(idx+1) for idx in range(SCREENS_COUNT)]
