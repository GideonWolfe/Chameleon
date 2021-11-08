#!/bin/sh

# Generates zathura configuration file

. $HOME/.cache/wal/colors.sh

cat <<CONF
[global]
    # Sort messages by urgency.
    sort = yes
    idle_threshold = 120
    font = Monospace 14
    line_height = 0
    markup = full
    # The format of the message.  Possible variables are:
    #   %a  appname
    #   %s  summary
    #   %b  body
    #   %i  iconname (including its path)
    #   %I  iconname (without its path)
    #   %p  progress value if set ([  0%] to [100%]) or nothing
    #   %n  progress value if set without any extra characters
    #   %%  Literal %
    # Markup is allowed
    format = "<b>%s</b>\n%b"
    alignment = left
    show_age_threshold = 60
    word_wrap = yes
    ellipsize = middle
    ignore_newline = no
    stack_duplicates = true
    hide_duplicate_count = true
    show_indicators = yes
    icon_position = left
    max_icon_size = 40
    sticky_history = yes
    history_length = 20
    dmenu = /usr/bin/dmenu -p dunst:
    browser = /usr/bin/firefox -new-tab
    # Always run rule-defined scripts, even if the notification is suppressed
    title = Dunst
    class = Dunst
    startup_notification = false
    force_xinerama = false
    monitor = 0
    follow = keyboard
    geometry = "350x5-0+24"
    indicate_hidden = yes
    shrink = yes
    transparency = 0
    notification_height = 0
    separator_height = 2
    padding = 0
    horizontal_padding = 8
    frame_width = 3
[experimental]
    per_monitor_dpi = false
[shortcuts]
    close = ctrl+space
    close_all = ctrl+shift+space
    history = ctrl+grave
    context = ctrl+shift+period
frame_color = "${cursor}"
separator_color = "${foreground}"
[base16_low]
    msg_urgency = low
    background = "${color0}"
    foreground = "${color1}"
[base16_normal]
    msg_urgency = normal
    background = "${background}"
    foreground = "${foreground}"
[base16_critical]
    msg_urgency = critical
    background = "${color15}"
    foreground = "${color14}"
CONF
