#!/bin/sh

# Generates gnuplot configuration file

. $HOME/.cache/wal/colors.sh

cat <<CONF
# Basic configs
set grid
set isosamples 50
set hidden3d
# Draw a background
set object rectangle from screen 0,0 to screen 1,1 behind fillcolor rgb '$background' fillstyle solid noborder
# Color some lines
set linetype 1 lw 2 lc rgb '$color6' pointtype 6
set linetype 2 lw 2 lc rgb '$foreground' pointtype 6
set linetype 3 lw 2 lc rgb '$color3' pointtype 6
# Key and border colors
set border lw 3 lc rgb '$color4'
set key textcolor rgb '$color2'
set xlabel "X" textcolor rgb '$color3'
set ylabel "Y" textcolor rgb '$color3'
CONF

