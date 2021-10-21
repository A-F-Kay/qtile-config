# Copyright (c) 2010 Aldo Cortesi Copyright (c) 2010, 2014 dequis Copyright (c) 2012 Randall Ma Copyright (c) 2012-2014 Tycho Andersen Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import socket
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

colors = [["#282c34", "#282c34"],  # panel background
          ["#3d3f4b", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#74438f", "#74438f"],  # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
          ["#e1acff", "#e1acff"],  # window name
          ["#ecbbfb", "#ecbbfb"]]  # backbround for inactive screens

# groups = [Group("WWW", {'layout': 'monadtall'}),
#           Group("DEV", {'layout': 'monadtall'}),
#           Group("SYS", {'layout': 'monadtall'}),
#           Group("DOC", {'layout': 'monadtall'}),
#           Group("VBOX", {'layout': 'monadtall'}),
#           Group("CHAT", {'layout': 'monadtall'}),
#           Group("MUS", {'layout': 'monadtall'}),
#           Group("VID", {'layout': 'monadtall'}),
#           Group("GFX", {'layout': 'floating'})]

groups = [Group(name) for name in [
    "CHAT", "DEV", "SYS", "WWW", "MUS", "VID"
]]


def window_to_another_screen(qtile):
    screen_idx = qtile.screens.index(qtile.current_screen)
    another_screen_idx = screen_idx - 1 if screen_idx > 0 else len(qtile.screens) - 1
    if another_screen_idx != 9000:
        group = qtile.screens[another_screen_idx].group.name
        qtile.current_window.togroup(group)


keys = [
    # Switch between windows
    Key([mod], "a", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "d", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "s", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "w", lazy.layout.up(), desc="Move focus up"),

    ### Switch focus to specific monitor (out of three)
    Key([mod], "q", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "a", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "d", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "s", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "w", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "a", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "d", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "s", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "w", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "k", lazy.window.kill(), desc="Kill focused window"),

    # @afkay
    Key([mod], "i", lazy.spawn("intellij-idea-ultimate-edition"),
        desc="Open Intellij IDEA"),
    Key([mod], "b", lazy.spawn("chromium"), desc="Open browser"),
    Key([mod], "t", lazy.spawn("telegram-desktop"),
        desc="Open Telegram messenger"),
    Key([mod], "o", lazy.spawn("discord"), desc="Open Disc_O_rd"),
    Key([mod], "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout"),
    Key([mod], "v",
        lazy.spawn("tor-browser"),
        desc="Open Tor Browser (VPN-like stuff so it's mapped to 'v')"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

group_idx = 0
for i in groups:
    group_idx += 1
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(group_idx), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(group_idx), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        border_focus='#F0D9FF',
        border_normal='#49454c',
        margin=4,
        border_width=2,
        border_on_single=False
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu Mono derivative Powerline',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty")}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Mono derivative Powerline",
            fontsize=13,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=5,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Prompt(
            prompt=prompt,
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.KeyboardLayout(
            foreground=colors[2],
            background=colors[5],
            padding=8,
            configured_keyboards=["us", "ru"],
            desc="Next keyboard layout"
        ),
        widget.Memory(
            measure_mem='G',
            format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ',
            foreground=colors[2],
            background=colors[4],
            mouse_callbacks={'Button1': lazy.spawn("alacritty" + ' -e htop')},
            padding=5
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[2],
            background=colors[5],
            padding=0
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[5],
            format="%A, %B %d - %H:%M ",
            padding=8
        ),
    ]
    return widgets_list


def make_screens():
    def make_screen():
        return Screen(
            top=bar.Bar(
                init_widgets_list(),
                24
            ),
        )

    screens_count = 2

    return [make_screen() for _ in range(screens_count)]


screens = make_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
