# Config File for Qtile WM

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

colors = [
    ["252525", "252525"],
    ["414141", "414141"],
    ["AF0404", "AF0404"]
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    
    ############################################
    ########## Launching Applications ##########
    ############################################

    Key(
        [mod], "Return", 
        lazy.spawn(terminal),
        desc="Launch Terminal"
    ),

    #######################################
    ########## Layout Navigation ########## 
    #######################################
    
    # Moving windows around the layout
    Key(
        [mod], "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        [mod], "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key(
        [mod], "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    Key(
        [mod], "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    
    # Resizing windows in the layout
    
    Key(
        [mod, "control"], "Left", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    Key(
        [mod, "control"], "Right", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),
    Key(
        [mod, "control"], "Down", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key(
        [mod, "control"], "Up", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        [mod], "space", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),
    
    # Toggle between different layouts as defined below
    Key(
        [mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),
    Key(
        [mod], "Escape", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),
    Key(
        [mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),
    Key(
        [mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
    Key(
        [mod], "r", 
        lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
	border_focus_stack=["#d75f5f", "#8f3d3d"],
	border_width=2,
	margin=6),
    layout.Max(
	margin=6),
    # Try more layouts by unleashing below layouts.
    layout.Stack(
	num_stacks=3,
	margin=6),
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
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line',
                    disable_drag=True,
                    margin=5
                ),
                
                widget.Prompt(),
                
                widget.TaskList(),

                widget.Spacer(
                    length=bar.STRETCH
                ),
                
                widget.TextBox(
                    "[ icon ]"
                ),
                
                widget.Spacer(
                    length=bar.STRETCH
                ),

                # widget.CPUGraph(),

                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                
                widget.Spacer(
                    length=bar.STRETCH
                ),

                # widget.PulseVolume(),
                widget.Volume(),

                widget.Systray(),
                
                # widget.OpenWeather(
                #     cityid="4160021"
                # ),
                
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p"
                ),
            ],
            24
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
    ]
)
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
