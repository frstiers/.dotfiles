# Config File for Qtile WM
import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

from settings.mouse import mouse
from settings.keys import keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import fake_screens
from settings.defaults import mod

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.run([home + '/.config/qtile/autostart.sh'])

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"