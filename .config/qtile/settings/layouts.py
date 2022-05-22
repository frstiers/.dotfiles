from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    'border_width': 1,
    'margin': 6,
    'border_focus': colors['focus'][0],
}

layouts = [
    layout.Columns(
        **layout_conf
    ),
    layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(
    #     num_stacks=2,
    #     margin=6
    # ),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        font = "Code New Roman",
        fontsize = 10,
        sections = ["Active Windows"],
        section_fontsize = 12,
        border_width = 2,
        bg_color = colors['dark'],
        active_bg = colors['focus'][0],
        active_fg = colors['dark'],
        inactive_bg = colors['grey'],
        inactive_fg = colors['dark'],
        padding_left = 0,
        padding_x = 0,
        padding_y = 5,
        section_top = 10,
        section_bottom = 20,
        level_shift = 8,
        vspace = 3,
        panel_width = 200,
    ),
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