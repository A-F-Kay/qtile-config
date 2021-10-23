from libqtile import widget, qtile

from afkay_config.const import WidgetColors, PowerlineColors, prompt
from afkay_config.widgets.MyCryptoTicker import MyCryptoTicker


def _make_powerline_left(*, background: str, foreground: str):
    return widget.TextBox(
        text=u" \ue0b2",
        foreground=foreground,
        background=background,
        fontsize=30,
        padding=0,
    )


def _make_powerline_right(*, background: str, foreground: str):
    return widget.TextBox(
        text=u"\ue0b0",
        foreground=foreground,
        background=background,
        fontsize=30,
        padding=0
    )


def make_widgets():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=WidgetColors.PanelBg,
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
            foreground=WidgetColors.PanelBg,
            background=WidgetColors.PanelBg
        ),
        widget.GroupBox(
            font="Source Code Pro Semibold",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=3,
            rounded=False,
            highlight_method="line",
            active=WidgetColors.DefaultFg,
            inactive=WidgetColors.InactiveScreenBg,
            highlight_color=WidgetColors.CurrentScreenTabBg,
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
            foreground=WidgetColors.PanelBg,
            background=WidgetColors.PanelBg
        ),
        widget.WindowName(
            foreground=WidgetColors.WindowNameFg,
            background=WidgetColors.PanelBg,
            padding=0,
            for_current_screen=True
        ),
        widget.Systray(
            background=WidgetColors.PanelBg,
            padding=5
        ),
        _make_powerline_left(**PowerlineColors.BeforeFirst),
        widget.KeyboardLayout(
            **WidgetColors.OddWidget,
            padding=8,
            configured_keyboards=["us", "ru"],
            desc="Next keyboard layout"
        ),
        _make_powerline_left(**PowerlineColors.BeforeEven),
        widget.CheckUpdates(
            **WidgetColors.EvenWidget,
            colour_no_updates=WidgetColors.EvenWidget['foreground'],
            color_have_update=WidgetColors.EvenWidget['foreground'],
            no_update_string="😊",
            update_interval=60*40
        ),
        _make_powerline_left(**PowerlineColors.BeforeOdd),
        MyCryptoTicker(
            **WidgetColors.OddWidget,
            currency='USD',
            amount_in_thousands=True,
            format="{crypto}: {symbol}{amount:.2f}K"
        ),
        _make_powerline_left(**PowerlineColors.BeforeEven),
        widget.CPU(
            **WidgetColors.EvenWidget,
            padding=8,
            format="CPU: {load_percent}%",
        ),
        _make_powerline_left(**PowerlineColors.BeforeOdd),
        widget.Memory(
            **WidgetColors.OddWidget,
            measure_mem='G',
            format='{MemUsed: .01f}{mm} /{MemTotal: .0f}{mm} ',
            padding=5
        ),
        _make_powerline_left(**PowerlineColors.BeforeEven),
        widget.TextBox(
            **WidgetColors.EvenWidget,
            text=" Vol:",
            padding=0
        ),
        widget.Volume(
            **WidgetColors.EvenWidget,
            padding=5
        ),
        _make_powerline_left(**PowerlineColors.BeforeOdd),
        widget.CurrentLayout(
            **WidgetColors.OddWidget,
            padding=5
        ),
        _make_powerline_left(**PowerlineColors.BeforeEven),
        widget.Clock(
            **WidgetColors.EvenWidget,
            format="%d/%m/%Y - %I:%M %p",
            padding=8
        ),
    ]
    return widgets_list
