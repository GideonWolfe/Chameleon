#!/bin/bash
# Author: Gideon Wolfe https://github.com/GideonWolfe
# Usage: theme [image] [other wal options]

# Check to make sure at least one argument was passed
if (( $# < 1 )); then
    echo "Wal needs at least one argument"
    exit 1
fi

echo "                      _       _._"
echo "               _,,-''' ''-,_ }'._''.,_.=._"
echo "            ,-'      _ _    '        (  @)'-,"
echo "          ,'  _..==;;::_::'-     __..----'''}"
echo "         :  .'::_;==''       ,'',: : : '' '}"
echo "        }  '::-'            /   },: : : :_,'"
echo "       :  :'     _..,,_    '., '._-,,,--\'    _"
echo "      :  ;   .-'       :      '-, ';,__\.\_.-'"
echo "     {   '  :    _,,,   :__,,--::',,}___}^}_.-'"
echo "     }        _,'__''',  ;_.-''_.-'"
echo "    :      ,':-''  ';, ;  ;_..-'"
echo "_.-' }    ,',' ,''',  : ^^"
echo "_.-''{    { ; ; ,', '  :"
echo "      }   } :  ;_,' ;  }"
echo "       {   ',',___,'   '"
echo "        ',           ,'"
echo "          '-,,__,,-'"
echo "   ________                         __               "
echo "   / ____/ /_  ____ _____ ___  ___  / /__  ____  ____ "
echo "  / /   / __ \/ __  / __  __ \/ _ \/ / _ \/ __ \/ __ \ "
echo " / /___/ / / / /_/ / / / / / /  __/ /  __/ /_/ / / / / "
echo " \____/_/ /_/\__,_/_/ /_/ /_/\___/_/\___/\____/_/ /_/ "





# Extract the filepath of the image and call wal on it
# You can pass wal command flags to this script and they are passed to wal
echo "########################"
echo "# Running Wal On Image #"
echo "########################"
FILEPATH=$(readlink -f "$1")
wal -i $FILEPATH ${@:2}
echo ""

# Set the GTK theme
# use lxappearance to select the oomox-xresources theme 
if [ -x "$(command -v oomox-cli)" ]; then
    echo "##########################"
    echo "# Updating GTK theme     #"
    echo "##########################"
    oomox-cli /opt/oomox/scripted_colors/xresources/xresources-reverse
    echo ""
fi

# Set the icon theme. Requires archdroid icons
# https://aur.archlinux.org/packages/archdroid-icon-theme/
# To use other icons, there are other oomox commands ie.
# oomox-gnome-colors-icons-cli
# use lxappearance to select the oomox-xresources-flat icon theme
if [ -d /usr/share/icons/Archdroid-Red ]; then
    echo "##########################"
    echo "# Updating Icon theme     #"
    echo "##########################"
    oomox-archdroid-icons-cli /opt/oomox/scripted_colors/xresources/xresources-reverse
    echo "Icon Theme Generated"
    echo ""
fi

# Set wallpaper to stretch all monitors
#feh $FILEPATH --bg-fill --no-xinerama

# Set the colors for telegram-desktop
# Chat background not setting for some reason, must set manually
if [ -x "$(command -v telegram-desktop)" ]; then
    if ! [ -d $HOME/.telegram-palette-gen/ ]; then
        echo "Install telegram palette gen: https://github.com/matgua/telegram-palette-gen"
    else
        echo "##########################"
        echo "# Updating Telegram Skin #"
        echo "##########################"
        $HOME/.telegram-palette-gen/telegram-palette-gen --wal
        echo ""
    fi
fi

# Updates steam skin (requires python-wal-steam-git from AUR)
# or https://github.com/kotajacob/wal_steam
if [ -x "$(command -v steam)" ]; then
    if ! [ -x "$(command -v wal_steam)" ]; then
        echo "Install wal_steam: https://github.com/kotajacob/wal_steam"
    else
        echo "#######################"
        echo "# Updating Steam Skin #"
        echo "#######################"
        wal_steam -w
        echo ""
    fi
fi

# Update Keyboard colors (corsair keyboards)
if [ -x "$(command -v ckb-next)" ]; then
    echo "###########################"
    echo "# Updating Keyboard Color #"
    echo "###########################"
    KEYBOARDCOLOR=$(cat $HOME/.cache/wal/colors.css | grep color6 | awk '{print $2}' | cut -c2- | rev | cut -c2- | rev)
    echo rgb $KEYBOARDCOLOR > /dev/input/ckb1/cmd
    echo "Keyboard Color Set"
    echo ""
fi

# Update Keyboard colors (razer keyboards)
if [ -x "$(command -v razer-cli)" ]; then
    echo "###########################"
    echo "# Updating Razer Devices Color #"
    echo "###########################"
    razer-cli -a
    echo "Razer Devices Color Set"
    echo ""
fi


# Update Spotify colors (requires app restart)
# You can opt for the GTK theme generated from oomox or spicetify wal theme
if [ -x "$(command -v spotify)" ]; then
    if [ -x "$(command -v oomoxify-cli)" ]; then
        echo "##########################"
        echo "# Updating Spotify Color #"
        echo "##########################"
        oomoxify-cli  $HOME/.cache/wal/colors-oomox -s /opt/spotify/Apps/
        echo "Spotify Theme Set"
        echo ""
    fi
    if [ -x "$(command -v spicetify)" ]; then
        echo "##########################"
        echo "# Updating Spotify Color #"
        echo "##########################"
        spicetify update
        echo "Spotify Theme Set"
        echo ""
    fi
fi

# Update Zathura colors (requires Zathura-Pywal)
if [ -x "$(command -v genzathurarc)" ]; then
    echo "##########################"
    echo "# Updating Zathura Color #"
    echo "##########################"
    genzathurarc > $HOME/.config/zathura/zathurarc
    echo "Zathura Theme Set"
    echo ""
fi

# Update Gnuplot colors (requires Gnuplot-Pywal)
if [ -x "$(command -v gengnuplotconfig)" ]; then
    echo "##########################"
    echo "# Updating Gnuplot Color #"
    echo "##########################"
    gengnuplotconfig > $HOME/.gnuplot
    echo "Gnuplot Theme Set"
    echo ""
fi

# Update IntelliJ colors (requires https://github.com/0x6C38/intellijPywal)
# Symlink intellijPywalGen.sh to /usr/bin or /usr/local/bin
# sudo ln -s /path/to/intelliJPywalGen.sh /usr/local/intelliJPywalGen
# You also must hardcode in your IntelliJ direcntory to pass into the script.
# example: intellijPywalGen $HOME/.IdeaIC2019.2/config/
if [ -x "$(command -v intelliJPywalGen)" ]; then
    CONFIGDIR=$HOME/.PyCharmCE2019.2/config/
    echo "##################################"
    echo "# Updating IntelliJ Color Scheme #"
    echo "##################################"
    intelliJPywalGen $CONFIGDIR
    echo "IntelliJ Theme Set"
    echo ""
fi


# Update leds (requires https://github.com/Paul-Houser/pyWalNeopixels)
if [ -x "$(command -v startLEDS)" ]; then
  echo "###########################"
  echo "# Updating PywalNeopixels #"
  echo "###########################"
  startLEDS
  echo "PywalNeopixels set"
  echo ""
fi

# Update Discord
if [ -x "$(command -v pywal-discord)" ]; then
  echo "###########################"
  echo "# Updating pywal-discord  #"
  echo "###########################"
  pywal-discord
  echo "Discord theme set"
  echo ""
fi


# update slickgreeter-pywal (requires https://github.com/paul-houser/slickgreeter-pywal)
if [ -x "$(command -v slick-pywal)" ]; then
  echo "##########################"
  echo "# updating slick-greeter #"
  echo "##########################"
  slick-pywal
  echo""
fi


# update pywalfox (requires https://github.com/Frewacom/Pywalfox)
# set variable to location of pywalfox.py
# /some/directory/Pywalfox/daemon
PYWALFOXDIR=$HOME/Programs/Pywalfox/daemon
if test -d "$PYWALFOXDIR"; then
 echo "####################"
 echo "# updating firefox #"
 echo "####################"
 python3 $PYWALFOXDIR/pywalfox.py update
 echo""
fi
