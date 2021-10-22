from enum import Enum

from libqtile import widget, qtile

from afkay_config.const import WidgetColors, prompt


class PowerlineDirection(Enum):
    RIGHT = "r"
    LEFT = "l"


def _make_powerline(direction: PowerlineDirection, *, fg: str, bg: str):
    if direction == PowerlineDirection.RIGHT:
        return [
            widget.TextBox(
                text=u"\ue0b0",
                foreground=fg,
                background=bg,
                fontsize=30,
                padding=0
            ),
            widget.Sep(padding=0, linewidth=0, background=bg),
        ]
    else:
        return [
            widget.Sep(padding=0, linewidth=0, background=bg),
            widget.TextBox(
                text=u" \ue0b2",
                foreground=fg,
                background=bg,
                fontsize=30,
                padding=0,
            ),
        ]


def make_widgets():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.PanelBg
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty")}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.PanelBg
        ),
        widget.GroupBox(
            font="Ubuntu Mono derivative Powerline",
            fontsize=13,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=3,
            active=WidgetColors.DefaultFg,
            inactive=WidgetColors.InactiveScreenBg,
            rounded=False,
            highlight_color=WidgetColors.CurrentScreenTabBg,
            highlight_method="line",
            this_current_screen_border=WidgetColors.WindowNameFg,
            this_screen_border=WidgetColors.OtherTabsBorder,
            other_current_screen_border=WidgetColors.WindowNameFg,
            other_screen_border=WidgetColors.OtherTabsBorder,
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.PanelBg
        ),
        widget.Prompt(
            prompt=prompt,
            padding=10,
            foreground=WidgetColors.PromptFg,
            background=WidgetColors.CurrentScreenTabBg
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.PanelBg
        ),
        widget.WindowName(
            foreground=WidgetColors.WindowNameFg,
            background=WidgetColors.PanelBg,
            padding=0
        ),
        widget.Systray(
            background=WidgetColors.PanelBg,
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=WidgetColors.PanelBg,
            background=WidgetColors.PanelBg
        ),
        *_make_powerline(PowerlineDirection.LEFT, bg=WidgetColors.PanelBg, fg=WidgetColors.EvenWidgetBg),
        widget.KeyboardLayout(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            padding=8,
            configured_keyboards=["us", "ru"],
            desc="Next keyboard layout"
        ),
        *_make_powerline(PowerlineDirection.LEFT, bg=WidgetColors.EvenWidgetBg, fg=WidgetColors.OtherTabsBorder),
        widget.Memory(
            measure_mem='G',
            format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ',
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.OddWidgetBg,
            padding=5
        ),
        *_make_powerline(PowerlineDirection.LEFT, fg=WidgetColors.EvenWidgetBg, bg=WidgetColors.OtherTabsBorder),
        widget.TextBox(
            text=" Vol:",
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            padding=0
        ),
        widget.Volume(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            padding=5
        ),
        *_make_powerline(PowerlineDirection.LEFT, bg=WidgetColors.EvenWidgetBg, fg=WidgetColors.OtherTabsBorder),
        widget.CurrentLayout(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.OddWidgetBg,
            padding=5
        ),
        *_make_powerline(PowerlineDirection.LEFT, fg=WidgetColors.EvenWidgetBg, bg=WidgetColors.OtherTabsBorder),
        widget.Clock(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            format="%A, %B %d - %H:%M ",
            padding=8
        ),
    ]
    return widgets_list
