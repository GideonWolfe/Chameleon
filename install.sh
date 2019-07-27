#!/bin/bash
FILEPATH=$(readlink -f "theme.sh")
echo $FILEPATH

ln -s $FILEPATH /usr/local/bin/theme
