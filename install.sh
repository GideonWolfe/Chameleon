#!/bin/bash
FILEPATH=$(readlink -f "theme.sh")

ln -s $FILEPATH /usr/local/bin/theme
