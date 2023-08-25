#!/bin/sh
userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/Xresources
sysmodmap=/etc/X11/xinit/Xmodmap

# merge in defaults and keymaps
if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi
if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi
if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi
if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs
#exec xbindkeys &
exec qtile start
#slstatus &
#clipmenud &
#keepassxc &
#feh --bg-scale ~/Bilder/back1.webp 
#picom &
# Führt einen session-dbus aus (rc startet system-dbus)
#exec dbus-launch --exit-with-session dwm > ~/.config/dwm/dwm.log 
