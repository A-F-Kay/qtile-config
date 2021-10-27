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
from typing import List  # noqa: F401

import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Click, Drag, Key, Match
from libqtile.lazy import lazy

from afkay_config import const
from afkay_config.keybindings.config import app_bindings, \
    direction_bindings, group_bindings
from afkay_config.layouts.const import layouts as afkay_layouts
# Unused. Needs to be imported to make hooks work
from afkay_config.layouts.utils import on_layout_change  # noqa: F401
from afkay_config.screens.const import SECONDARY_SCREEN, MAIN_SCREEN
from afkay_config.screens.utils import make_screens

mod = const.mod
terminal = const.terminal
prompt = const.prompt
groups = const.groups
layouts = afkay_layouts

keys = [
    ### Switch focus to specific monitor (out of three)
    Key([mod], "q", lazy.to_screen(SECONDARY_SCREEN), desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(MAIN_SCREEN), desc='Keyboard focus to monitor 2'),

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
    Key([mod], "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

keys.extend(app_bindings)
keys.extend(direction_bindings)
keys.extend(group_bindings)

screens = make_screens()





widget_defaults = dict(
    font='Ubuntu Mono derivative Powerline',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

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
bring_front_click = False
cursor_warp = False
follow_mouse_focus = False

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

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call(['bash', '/home/afkay/.config/qtile/afkay_config/scripts/autostart.sh'])


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
