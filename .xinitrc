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
slstatus &
clipmenud &
keepassxc &
owncloudcmd -u 6FQ9M2@rwth-aachen.de -p Fmhs1RijHUDCR7o9YOAp ~/Sciebo https://rwth-aachen.sciebo.de &
# Führt einen session-dbus aus (rc startet system-dbus)
exec dbus-launch --exit-with-session dwm > ~/.config/dwm/dwm.log 
