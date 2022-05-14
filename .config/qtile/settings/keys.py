from libqtile.config import Key, Match
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from .groups import groups
from .defaults import *

###############################
########## Functions ##########
###############################

def go_to_app_or_group(group, app):
    def temp_function(qtile):
        try:
            qtile.groups_map[group].cmd_toscreen()
            qtile.cmd_spawn(app)
        except KeyError:
            qtile.cmd_spawn(app)
    return temp_function

def launchDefaultApp(qtile):
    # Defines the default app based on the current group
    if qtile.current_group.name == "1":
        defaultApp = terminal
    elif qtile.current_group.name == "2":
        defaultApp = webBrowser
    elif qtile.current_group.name == "3":
        defaultApp = codeEditor
    elif qtile.current_group.name == "4":
        defaultApp = "steam"
    elif qtile.current_group.name == "6":
        defaultApp = webBrowser
    elif qtile.current_group.name == "7":
        defaultApp = "discord"
    elif qtile.current_group.name == "8":
        defaultApp = "obsidian"
    else:
        defaultApp = terminal
    
    # Creates a list of windows in the current group
    currentWindows = [ w for w in qtile.windows_map.values() if w.group == qtile.current_group ]
    appExists = False

    # Check if the default app already exists in the group or not; if it does focus it, else spawn it
    for currentWindow in currentWindows:
        if defaultApp.lower() in currentWindow.name.lower():
            appExists = True
            appWindow = currentWindow
            break

    if appExists:
        qtile.current_screen.set_group(currentWindow.group)
        currentWindow.group.focus(currentWindow, False)
    else:
        qtile.cmd_spawn(defaultApp)

def cycleOpenApps(qtile):
    ''' 
    TODO: build out a function that cycles through a list of open windows and 
    changes focus to that group and screen
    '''

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    
    #########################################
    ########## General Keybindings ##########
    #########################################

    Key(
        [mod], "l", 
        lazy.spawn(lockscreen),
        desc="Lock the screen."
    ),

    Key(
        [mod, "shift"], "period", 
        lazy.next_screen(),
        desc=""
    ),

    ############################################
    ########## Launching Applications ##########
    ############################################

    Key(
        [mod], "Return", 
        lazy.spawn(terminal),
        desc="Launch Terminal"
    ),
    Key(
        ["control"], "space",
        lazy.function(launchDefaultApp),
        desc="Launch current group's default application"
    ),
    Key(
        [mod], "space", 
        lazy.spawn(runLauncher), 
        desc="Launch run launcher"
    ),
    Key(
        [mod], "d",
        lazy.function(go_to_app_or_group("7", "discord")),
        desc="Launch or go to discord"
    ),
    Key(
        [mod], "c",
        lazy.function(go_to_app_or_group("3", "vscodium")),
        desc="Launch or go to code editor"
    ),
    Key(
        [mod, "shift"], "s",
        lazy.spawn(screenshot),
        desc="Launches screenshot tool"
    ),

    # Key(
    #     [mod], "i",
    #     lazy.function(go_to_app_or_group("2", "chromium")),
    #     desc="Launch or go to internet browser"
    # ),

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
        [mod, "shift"], "Right",
        lazy.screen.next_group()
    ),
    Key(
        [mod, "shift"], "Left",
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