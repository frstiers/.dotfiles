#!/bin/sh
picom --config $HOME/.config/picom/picom.conf &
feh --no-fehbg --bg-center $HOME/.config/wallpaper.jpg &
# onedrive --monitor &
conky &
flameshot &
