import os
import socket

from afkay_config.colors import DtColors
from afkay_config.utils import make_colors
from afkay_config.groups.utils import make_groups

# SUPER("WIN") key
mod = 'mod4'
# Alt key
alt = 'mod1'

terminal = 'alacritty'
prompt = f"{os.environ['USER']}@{socket.gethostname()}: "
groups = make_groups()

check_updates_interval_minutes = 40


class WidgetColors:
    PanelBg = make_colors(DtColors.PanelBg)
    DefaultFg = make_colors(DtColors.DefaultFg)

    InactiveScreenBg = make_colors(DtColors.InactiveScreenBg)
    CurrentScreenTabBg = make_colors(DtColors.CurrentScreenTabBg)
    OtherTabsBorder = make_colors(DtColors.OtherTabsBorder)
    PromptFg = make_colors(DtColors.PromptFg)
    WindowNameFg = make_colors(DtColors.WindowNameFg)

    OddWidget = {
        'foreground': DtColors.DefaultFg,
        'background': DtColors.OtherTabsBorder,
    }
    EvenWidget = {
        'foreground': DtColors.DefaultFg,
        'background': DtColors.EvenWidgetBg
    }


class PowerlineColors:
    BeforeFirst = {
        'background': WidgetColors.PanelBg,
        'foreground': WidgetColors.OddWidget['background'],
    }
    BeforeEven = {
        'background': WidgetColors.OddWidget['background'],
        'foreground': WidgetColors.EvenWidget['background'],
    }
    BeforeOdd = {
        'background': WidgetColors.EvenWidget['background'],
        'foreground': WidgetColors.OddWidget['background'],
    }
