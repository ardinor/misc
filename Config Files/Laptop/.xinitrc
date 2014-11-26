#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

#export GTK_IM_MODULE='uim'
#export QT_IM_MODULE='uim'
#uim-xim &
#export XMODIFIERS='@im=uim'

#uim-toolbar-gtk &
#uim-toolbar-gtk3 &
#uim-toolbar-gtk3-systray &
# exec gnome-session
# exec startkde
# exec startxfce4
# ...or the Window Manager of your choice
#exec cinnamon-session

# Since we're not using a WM, merge Xresources in here
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

session=${1:-cinnamon}

case $session in
    i3|i3wm         ) exec i3;;
    cinnamon        ) exec cinnamon-session;;
    *) exec $1;;
esac
