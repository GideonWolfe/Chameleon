#!/bin/bash
FILEPATH=$(readlink -f "theme.sh")

ln -s $FILEPATH /usr/local/bin/chameleon

# make the directory for the lightdm background image with the correct permissions.
if ! [ -d /usr/share/wallpapers ]; then
  mkdir /usr/share/wallpapers
fi
chmod 777 /usr/share/wallpapers

# generate the config for slick-greeter if it doesn't already exist
slickconf="/etc/lightdm/slick-greeter.conf"
if ! [[ -f $slickconf ]]; then
  touch $slickconf
  echo "[Greeter]" >> $slickconf
  echo "background=/usr/share/wallpapers/wal" >> $slickconf
else
  sed -i.chmlnbk "s/background=.*/background=\/usr\/share\/wallpapers\/wal/g" /etc/lightdm/slick-greeter.conf
fi
