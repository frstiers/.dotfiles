from libqtile.config import Screen
from libqtile import bar, widget
from libqtile.log_utils import logger

from .theme import colors

from .widgets import topPrimaryWidgets, topSecondaryWidgets, bottomPrimaryWidgets, bottomSecondaryWidgets

import subprocess

def top_bar(widgets):
    return bar.Bar(widgets, 32, background = colors['dark'])

def bottom_bar(widgets):
    return bar.Bar(widgets, 28, background = colors['dark'])

# screens = [
#     Screen(
#         top=top_bar(topPrimaryWidgets),
#         bottom=bottom_bar(bottomPrimaryWidgets)
#     ),
#     Screen(
#         top=top_bar(topSecondaryWidgets),
#         bottom=bottom_bar(bottomSecondaryWidgets)
#     ),
# ]

fake_screens = [
    Screen(
        top=top_bar(topPrimaryWidgets),
        bottom=bottom_bar(bottomPrimaryWidgets),
        x=0,
        y=0,
        width=1920,
        height=1080,
    ),
    Screen(
        top=top_bar(topSecondaryWidgets),
        bottom=bottom_bar(bottomSecondaryWidgets),
        x=1920,
        y=0,
        width=1920,
        height=1080,
    ),
]
