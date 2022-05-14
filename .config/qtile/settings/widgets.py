from libqtile import widget, bar, qtile

from .theme import colors
from .defaults import terminal

import os

home = '{HOME}'.format(**os.environ)

#################################
##### Defining Base Widgets #####
#################################

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def myGroupBox(visibleGroups=[]):
    return widget.GroupBox(
        **base(fg='light'),
        font='Code New Roman',
        fontsize=20,
        margin_y=3,
        margin_x=5,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=True,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True,
        visible_groups= visibleGroups
    )

def mySpacer():
    return widget.Spacer(
        length=bar.STRETCH
    )

def mySeparator():
    return widget.Sep(
        background=colors['dark'],
        foreground=colors['grey'],
        linewidth=3,
        padding=10
    )

def myCenterIcon(icon):
    return widget.TextBox(
        icon,
        fontsize = "24"
    )

def myCheckUpdates():
    return widget.CheckUpdates(
        distro='Arch_paru',
        no_update_string='0 ',
        display_format='{updates} ',
        mouse_callbacks = {
            'Button1': lambda: qtile.cmd_spawn(terminal)
        }
    )

def myQuickExit():
    return widget.TextBox(
        "襤",
        fontsize=24,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(home + "/.config/rofi/powermenu/powermenu.sh")
        }
    )

def myCurrentLayoutIcons():
    return widget.CurrentLayoutIcon(
        scale=0.75
    )

def myOpenWeather():
    return widget.OpenWeather(
        cityid="4160021",
        metric=False,
        format='{main_temp}° {units_temperature}'
    )

def myClock():
    return widget.Clock(
        format="%A, %B %d, %Y %H:%M"
    )

def myVolumeControl():
    return widget.PulseVolume()

def mySystemTray():
    return widget.Systray(
        padding=10
    )


#################################
##### Creating Widget Lists #####
#################################

topPrimaryWidgets = [
    myGroupBox(visibleGroups=['1', '2', '3', '4']),
    mySpacer(),
    myCenterIcon(icon=""),
    mySpacer(),
]

topSecondaryWidgets = [
    myGroupBox(visibleGroups=['5', '6', '7', '8', '9']),
    mySpacer(),
    myCenterIcon(icon=""),
    mySpacer(),
    mySystemTray(),
    mySeparator(),
    myCheckUpdates(),
    mySeparator(),
    myQuickExit(),
]

bottomPrimaryWidgets = [
    myCurrentLayoutIcons(),
    
    mySpacer(),
]

bottomSecondaryWidgets = [
    myCurrentLayoutIcons(),
    mySpacer(),

    mySeparator(),
    myVolumeControl(),
    mySeparator(),
    myOpenWeather(),
    mySeparator(),
    myClock(),
]

widget_defaults = {
    'font': 'Code New Roman',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
