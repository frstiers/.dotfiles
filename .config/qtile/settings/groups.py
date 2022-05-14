from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy

groups = [

    ##### Groups for Primary Display #####
    Group(
        name="1",
        label="", # Arch-Home 1
        position=1
    ),
    Group(
        name="2",
        label="", # Web browsing 1
        position=2
    ),
    Group(
        name="3",
        label="", # Programming
        position=3
    ),
    Group(
        name="4",
        label="", # Gaming
        position=4
    ),

    ##### Groups for Secondary Display #####

    Group(
        name="5",
        label="", # Arch-Home 2
        position=5
    ),
    Group(
        name="6",
        label="", # Web browsing 2
        position=6
    ),
    Group(
        name="7",
        label="", # Chat
        position=7
    ),
    Group(
        name="8",
        label="", # Notes
        position=8
    ),
    Group(
        name="9",
        label="", # Experimenting
        position=9
    ),
]