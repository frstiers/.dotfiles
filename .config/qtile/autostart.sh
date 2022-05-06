#!/bin/sh
picom --config $HOME/.config/picom/picom.conf &
conky &
feh --no-fehbg --bg-center $HOME/.config/wallpaper.jpg &