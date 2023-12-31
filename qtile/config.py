# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile.widget import backlight
from libqtile.dgroups import simple_key_binder

mod = "mod4"
terminal = guess_terminal()

# KEYS #################################################################
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "v", lazy.spawn("clipmenu"), desc="Launch clipmenu clipboard manager"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key(['mod4'], 'p', lazy.run_extension(extension.DmenuRun( # Dmenu
        dmenu_prompt=">",
        #dmenu_font="Andika-8",
        #background="#15181a",
        #foreground="#00ff00",
        #selected_background="#079822",
        #selected_foreground="#fff",
    ))),

    Key([],"XF86MonBrightnessUp",lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.UP)), # Change Backlight 
    Key([],"XF86MonBrightnessDown",lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.DOWN)),
    
    Key([],"XF86AudioLowerVolume",lazy.widget['volume'].decrease_vol()), # Decrease Volume 
    Key([],"XF86AudioRaiseVolume",lazy.widget['volume'].increase_vol()), # Increase Volume 
    Key([],"XF86AudioMute",lazy.widget['volume'].mute()), # Mute Volume
    
    Key([mod, "shift"], "End", lazy.spawn("doas /sbin/halt"), desc="Shutdown"),
]

# GROUPS #################################################################

#groups = [Group(i) for i in "123456789"]
groups = [
    Group("1",label=""),
    Group("2",label=""),
    Group("3"),
    Group("4"),
    Group("5",label="", matches=[Match(wm_class=["KeePassXC"])]),
]

# allow mod3+1 through mod3+0 to bind to groups; if you bind your groups
# by hand in your config, you don't need to do this.
#dgroups_key_binder = simple_key_binder(mod)

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
                lazy.window.togroup(i.name),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# LAYOUTS #################################################################

layouts = [
    layout.Columns(border_focus_stack = ["#d75f5f", "#8f3d3d"], border_width=4, margin=6),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
     layout.Stack(num_stacks=2),
     layout.Bsp(),
     layout.Matrix(),
     layout.MonadTall(),
     layout.MonadWide(),
     layout.RatioTile(),
     layout.Tile(),
     layout.TreeTab(),
     layout.VerticalTile(),
    #layout.Zoomy(),
]


# WIDGETS & SCREENS #################################################################

widget_defaults = dict(
    font="Inconsolata",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.CurrentLayout(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
                chords_colors={"launch": ("#ff0000", "#ffffff"),},
                    name_transform=lambda name: name.upper(),
        ),
        # widget.TextBox("default config", name="default"),
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.OpenWeather(
            app_key="4aa7e600f2bf00a63fbdee515b68cf06",
            location="Aachen",
            language="de",
            fmt = '  {}'
            ),
        widget.Sep(),
        widget.Systray(),
        widget.Sep(),
        widget.Volume(
            fmt = ' {}',
            ),
        widget.Sep(),
        widget.Battery(
            format="'{percent:2.0%} {watt:.2f} W'",
            fmt = ' {}'
            ),
        widget.Sep(),
        widget.Backlight(
            backlight_name="amdgpu_bl0",
            fmt = ' {}'
            ),
        widget.Sep(),
        widget.Clock(format="%d.%m %a %H:%M %p"),
        ]
    return widgets_list

# Monitor 1 will display ALL widgets in widgets_list. It is important that this
# is the only monitor that displays all widgets because the systray widget will
# crash if you try to run multiple instances of it.
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1 

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[6:8]
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=24, opacity = 0.7)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=24, opacity = 0.7))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

# FLOATING #################################################################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),     # gitk
        Match(wm_class="makebranch"),       # gitk
        Match(wm_class="maketag"),          # gitk
        Match(wm_class="ssh-askpass"),      # ssh-askpass
        Match(title="branchdialog"),        # gitk
        Match(title="pinentry"),            # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once # Autostart pipewire
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
