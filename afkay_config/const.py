import os
import socket

from afkay_config.colors import DtColors
from afkay_config.utils import make_colors, make_groups

# SUPER("WIN") key
mod = 'mod4'
terminal = 'alacritty'
prompt = f"{os.environ['USER']}@{socket.gethostname()}: "
groups = make_groups()


class WidgetColors:
    PanelBg = make_colors(DtColors.PanelBg)
    CurrentScreenTabBg = make_colors(DtColors.CurrentScreenTabBg)
    DefaultFg = make_colors(DtColors.DefaultFg)
    PromptFg = make_colors(DtColors.PromptFg)
    OtherTabsBorder = make_colors(DtColors.OtherTabsBorder)
    OddWidgetBg = make_colors(DtColors.OtherTabsBorder)
    EvenWidgetBg = make_colors(DtColors.EvenWidgetBg)
    WindowNameFg = make_colors(DtColors.WindowNameFg)
    InactiveScreenBg = make_colors(DtColors.InactiveScreenBg)
