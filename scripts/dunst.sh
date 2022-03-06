#!/bin/sh

# Generates zathura configuration file

. $HOME/.cache/wal/colors.sh

cat <<CONF
[global]
  ### Display ###

  # Which monitor should the notifications be displayed on.
  monitor = 0

  # Display notification on focused monitor.  Possible modes are:
  #   mouse: follow mouse pointer
  #   keyboard: follow window with keyboard focus
  #   none: don't follow anything
  #
  # "keyboard" needs a window manager that exports the
  # _NET_ACTIVE_WINDOW property.
  # This should be the case for almost all modern window managers.
  #
  # If this option is set to mouse or keyboard, the monitor option
  # will be ignored.
  follow = mouse

  # Show how many messages are currently hidden (because of geometry).
  indicate_hidden = yes

  # Shrink window if it's smaller than the width.  Will be ignored if
  # width is 0.
  shrink = no

  # The transparency of the window.  Range: [0; 100].
  # This option will only work if a compositing window manager is
  # present (e.g. xcompmgr, compiz, etc.).
  transparency = 10

  # Draw a line of "separator_height" pixel height between two
  # notifications.
  # Set to 0 to disable.
  separator_height = 2

  # Padding between text and separator.
  padding = 8

  # Horizontal padding.
  horizontal_padding = 8

  # Defines width in pixels of frame around the notification window.
  # Set to 0 to disable.
  frame_width = 3

  # Defines color of the frame around the notification window.
  frame_color = "#9aa8c8"

  # Define a color for the separator.
  # possible values are:
  #  * auto: dunst tries to find a color fitting to the background;
  #  * foreground: use the same color as the foreground;
  #  * frame: use the same color as the frame;
  #  * anything else will be interpreted as a X color.
  separator_color = auto

  # Sort messages by urgency.
  sort = yes

  # Don't remove messages, if the user is idle (no mouse or keyboard input)
  # for longer than idle_threshold seconds.
  # Set to 0 to disable.
  # A client can set the 'transient' hint to bypass this. See the rules
  # section for how to disable this if necessary
  idle_threshold = 120

  ### Text ###
  font = Hack Nerd Font 10

  # The spacing between lines.  If the height is smaller than the
  # font height, it will get raised to the font height.
  line_height = 0

  # Possible values are:
  # full: Allow a small subset of html markup in notifications:
  #        <b>bold</b>
  #        <i>italic</i>
  #        <s>strikethrough</s>
  #        <u>underline</u>
  #
  #        For a complete reference see
  #        <http://developer.gnome.org/pango/stable/PangoMarkupFormat.html>.
  #
  # strip: This setting is provided for compatibility with some broken
  #        clients that send markup even though it's not enabled on the
  #        server. Dunst will try to strip the markup but the parsing is
  #        simplistic so using this option outside of matching rules for
  #        specific applications *IS GREATLY DISCOURAGED*.
  #
  # no:    Disable markup parsing, incoming notifications will be treated as
  #        plain text. Dunst will not advertise that it has the body-markup
  #        capability if this is set as a global setting.
  #
  # It's important to note that markup inside the format option will be parsed
  # regardless of what this is set to.
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
  format = "<b><i>%s</i></b>\n%b"

  # Alignment of message text.
  # Possible values are "left", "center" and "right".
  alignment = center

  # Show age of message if message is older than show_age_threshold
  # seconds.
  # Set to -1 to disable.
  show_age_threshold = 120

  # Split notifications into multiple lines if they don't fit into
  # geometry.
  word_wrap = yes

  # When word_wrap is set to no, specify where to make an ellipsis in long lines.
  # Possible values are "start", "middle" and "end".
  ellipsize = middle

  # Ignore newlines '\n' in notifications.
  ignore_newline = no

  # Stack together notifications with the same content
  stack_duplicates = true

  # Hide the count of stacked notifications with the same content
  hide_duplicate_count = false

  # Display indicators for URLs (U) and actions (A).
  show_indicators = yes

  ### Icons ###

  # Align icons left/right/off
  icon_position = left

  # Scale larger icons down to this size, set to 0 to disable
  max_icon_size = 45

  # Paths to default icons.
  icon_path = /usr/share/icons/gnome/16x16/status/:/usr/share/icons/gnome/16x16/devices/

  ### History ###

  # Should a notification popped up from history be sticky or timeout
  # as if it would normally do.
  sticky_history = yes

  # Maximum amount of notifications kept in history
  history_length = 20

  ### Misc/Advanced ###

  # Browser for opening urls in context menu.
  browser = /usr/bin/google-chrome-stable

  # Always run rule-defined scripts, even if the notification is suppressed
  always_run_script = true

  # Define the title of the windows spawned by dunst
  title = Dunst

  # Define the class of the windows spawned by dunst
  class = Dunst

  # Define the corner radius of the notification window
  # in pixel size. If the radius is 0, you have no rounded
  # corners.
  # The radius will be automatically lowered if it exceeds half of the
  # notification height to avoid clipping text and/or icons.
  corner_radius = 5

  ### Legacy

  # Use the Xinerama extension instead of RandR for multi-monitor support.
  # This setting is provided for compatibility with older nVidia drivers that
  # do not support RandR and using it on systems that support RandR is highly
  # discouraged.
  #
  # By enabling this setting dunst will not be able to detect when a monitor
  # is connected or disconnected which might break follow mode if the screen
  # layout changes.
  force_xinerama = false

  ### mouse

  # Defines action of mouse event
  # Possible values are:
  # * none: Don't do anything.
  # * do_action: If the notification has exactly one action, or one is marked as default,
  #              invoke it. If there are multiple and no default, open the context menu.
  # * close_current: Close current notification.
  # * close_all: Close all notifications.
  mouse_left_click = do_action
  mouse_middle_click = close_all
  mouse_right_click = close_current

# Experimental features that may or may not work correctly. Do not expect them
# to have a consistent behaviour across releases.
[experimental]
  # Calculate the dpi to use on a per-monitor basis.
  # If this setting is enabled the Xft.dpi value will be ignored and instead
  # dunst will attempt to calculate an appropriate dpi value for each monitor
  # using the resolution and physical size. This might be useful in setups
  # where there are multiple screens with very different dpi values.
  per_monitor_dpi = false

[urgency_low]
    # IMPORTANT: colors have to be defined in quotation marks.
    # Otherwise the "#" and following would be interpreted as a comment.
    background = "${color0}"
    foreground = "${color1}"
    # Icon for notifications with low urgency, uncomment to enable
    icon = ${HOME}/.config/dunst/normal.png

[urgency_normal]
    background = "${background}"
    foreground = "${foreground}"
    # Icon for notifications with normal urgency, uncomment to enable
    icon = ${HOME}/.config/dunst/normal.png

[urgency_critical]
    background = "#900000"
    foreground = "#ffffff"
    frame_color = "#ff0000"
    # Icon for notifications with critical urgency, uncomment to enable
    icon = ${HOME}/.config/dunst/critical.png
CONF
