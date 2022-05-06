from libqtile import widget, bar, qtile
from .theme import colors

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

top_widgets = [
    
    widget.GroupBox(
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
        disable_drag=True
    ),
    widget.Spacer(
        length=bar.STRETCH
    ),
    widget.TextBox(
        "",
        fontsize="24"
    ),
    
    widget.Spacer(
        length=bar.STRETCH
    ),

    # widget.CPUGraph(),

    widget.CheckUpdates(
        distro='Arch_paru',
        no_update_string='Updates: None',
        execute='alacritty --hold -e sudo paru'
        # mouse_callbacks = 
        #     'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo paru')
        # }
    ),

    widget.Sep(
        background=colors['dark'],
        foreground=colors['grey'],
        linewidth=3,
        padding=10
    ),

    # widget.QuickExit(),
    widget.TextBox(
        "  ",
        fontsize=24,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("/home/frstiers/.config/rofi/powermenu/powermenu.sh")
            # "Button1": lambda: qtile.cmd_spawn("rofi -show power-menu -modi 'power-menu:/home/frstiers/.config/rofi/scripts/rofi-power-menu' ")
        }
    )
]

# def remove_window_name(text):
#     return ""

bottom_widgets = [

    # widget.CurrentLayout(),
    widget.CurrentLayoutIcon(
        scale=0.75
    ),

    widget.Spacer(
        length=bar.STRETCH
    ),

    # widget.TaskList(
    #     highlight_method='block',
    #     title_width_method=None,
    #     max_title_width=None,
    #     padding=6,
    #     border=colors['color1'],
    #     # parse_text=remove_window_name
    # ),
    
    widget.Spacer(
        length=bar.STRETCH
    ),

    widget.Sep(
        background=colors['dark'],
        foreground=colors['grey'],
        linewidth=3,
        padding=10
    ),
    
    widget.OpenWeather(
        cityid="4160021",
        metric=False,
        format='{main_temp}° {units_temperature}'
    ),
    
    widget.Sep(
        background=colors['dark'],
        foreground=colors['grey'],
        linewidth=3,
        padding=10
    ),
    
    widget.Clock(
        format="%A, %B %d, %Y %H:%M"
    ),

    widget.Sep(
        background=colors['dark'],
        foreground=colors['grey'],
        linewidth=3,
        padding=10
    ),

    widget.PulseVolume(),
    # widget.Volume(),
    
    widget.Systray(),
]

widget_defaults = {
    'font': 'Code New Roman',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()