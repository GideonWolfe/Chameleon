#!/bin/bash
# Set the colors for telegram-desktop
# Chat background not setting for some reason, must set manually

if [ -x "$(command -v intelliJPywalGen)" ]; then
    CONFIGDIR=$HOME/.IdeaIC2019.2/config/
    echo "##################################"
    echo "# Updating IntelliJ Color Scheme #"
    echo "##################################"
    intelliJPywalGen $CONFIGDIR
    echo "IntelliJ Theme Set"
    echo ""
fi
