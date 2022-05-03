from libqtile.config import Key
from libqtile.lazy import lazy

from .groups import groups

# Variables
mod = "mod4"
terminal = "alacritty"
runLauncher = "rofi -show drun"
# altTab = "rofi -show window"

# Functions

def go_to_app_or_group(group, app):
    def temp_function(qtile):
        try:
            qtile.groups_map[group].cmd_toscreen()
            qtile.cmd_spawn(app)
        except KeyError:
            qtile.cmd_spawn(app)
    return temp_function


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
    Key(
        [mod], "space", 
        lazy.spawn(runLauncher), 
        desc="Launch run launcher"
    ),
    Key(
        [mod], "d",
        lazy.function(go_to_app_or_group("3", "discord")),
        desc="Launch or go to discord"
    ),
    Key(
        [mod], "c",
        lazy.function(go_to_app_or_group("6", "vscodium")),
        desc="Launch or go to code editor"
    ),
    Key(
        [mod], "i",
        lazy.function(go_to_app_or_group("2", "chromium")),
        desc="Launch or go to internet browser"
    ),

    ############################################
    ################ Navigation ################
    ############################################
    
    # Moving Windows in current group
    Key(
        ["mod1"], "Tab",
        lazy.layout.next(),
        desc="Switch Windows in current group"
    ),
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
    
    # Resizing windows in the current group
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
    
    # Navigate between groups
    Key(
        ["mod1"], "Right",
        lazy.screen.next_group()
    ),
    Key(
        ["mod1"], "Left",
        lazy.screen.prev_group()
    ),

    # Toggle windows into fullscreen and floating modes
    Key(
        ["mod1"], "Up",
        lazy.window.toggle_fullscreen(),
        desc="Toggle focused window to/from fullscreen mode"
    ),
    Key(
        ["mod1"], "Down",
        lazy.window.toggle_floating(),
        desc="Toggle focused window to/from floating mode"
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
    
    
]