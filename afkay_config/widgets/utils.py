from libqtile import widget, qtile
from libqtile.lazy import lazy

from afkay_config.const import WidgetColors, prompt


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
        widget.KeyboardLayout(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            padding=8,
            configured_keyboards=["us", "ru"],
            desc="Next keyboard layout"
        ),
        widget.Memory(
            measure_mem='G',
            format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ',
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.OddWidgetBg,
            mouse_callbacks={'Button1': lazy.spawn("alacritty" + ' -e htop')},
            padding=5
        ),
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
        widget.CurrentLayout(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.OddWidgetBg,
            padding=5
        ),
        widget.Clock(
            foreground=WidgetColors.DefaultFg,
            background=WidgetColors.EvenWidgetBg,
            format="%A, %B %d - %H:%M ",
            padding=8
        ),
    ]
    return widgets_list
