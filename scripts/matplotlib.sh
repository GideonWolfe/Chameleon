#!/usr/bin/env bash

# Generates xfce4-terminal configuration file

. $HOME/.cache/wal/colors.sh

cat <<CONF
# Color for X and Y tick labels
xtick.color: ${foreground:1}
ytick.color: ${foreground:1}
# Display Grid
axes.grid: True
# Grid color
grid.color: ${foreground:1}
# Transparency
grid.alpha: 0.5
# Colors for line numbers
axes.prop_cycle: cycler('color', ['${color2:1}', '${color3:1}', '${color4:1}', '${color4:1}', '${color5:1}', '${color6:1}', '${color7:1}', '${color8:1}', '${color9:1}', '${color10:1}'])
# Axes Edge Color
axes.edgecolor: ${color6:1}
# Background color around graph
figure.facecolor: ${background:1}
# Axes title color
axes.titlecolor: ${foreground:1}
axes.labelcolor: ${foreground:1}
text.color: ${foreground:1}
# Background Color
axes.facecolor: ${background:1}
CONF
