from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger

from .theme import colors

from .widgets import top_widgets, bottom_widgets

import subprocess

def top_bar(widgets):
    return bar.Bar(widgets, 32, background = colors['dark'])

def bottom_bar(widgets):
    return bar.Bar(widgets, 28, background = colors['dark'])

screens = [
    Screen(
        top=top_bar(top_widgets),
        bottom=bottom_bar(bottom_widgets)
    )
]