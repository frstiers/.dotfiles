from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Columns(
        border_focus=colors['color1'],
        border_width=2,
        margin=6
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(
    #     num_stacks=3,
    #     margin=6
    # ),
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

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Conky"),
        Match(wm_class="Steam"),
        Match(wm_class="Steam Guard - Computer Authorization Required"),
        Match(wm_class="Steam - News")
    ],
    border_focus=colors["color4"][0]
)