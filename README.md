```
                      _       _._
               _,,-''' ''-,_ }'._''.,_.=._
            ,-'      _ _    '        (  @)'-,
          ,'  _..==;;::_::'-     __..----'''}
         :  .'::_;==''       ,'',: : : '' '}
        }  '::-'            /   },: : : :_,'
       :  :'     _..,,_    '., '._-,,,--\'    _
      :  ;   .-'       :      '-, ';,__\.\_.-'
     {   '  :    _,,,   :__,,--::',,}___}^}_.-'
     }        _,'__''',  ;_.-''_.-'
    :      ,':-''  ';, ;  ;_..-'
_.-' }    ,',' ,''',  : ^^
_.-''{    { ; ; ,', '  :
      }   } :  ;_,' ;  }
       {   ',',___,'   '
        ',           ,'
          '-,,__,,-'
```


This script acts as an extension to wal, by taking the generated colors and theming anything that can be themed, all in one script. 

If the script detects you have certain programs on your system, it will try to generate themes for them.

The current programs are ones that I use, but feel free to add more and send a PR!

# Examples

![alt-text](https://i.imgur.com/C3znJJJ.png)

Programs that use GTK themes like Thunar and Baobab should just pick up the theme, assuming you have selected the `oomox-xresources-reverse` theme in `lxappearance`. Spotify and Telegram shown here rocking their custom generated themes.

![alt-text](https://i.imgur.com/j4SEVpE.png)

Programs that use Qt themes can also be configured to take themes from GTK, meaning we can theme them as well! The programs must be launched with the `--style gtk2` flag, and you must install and configure [qt5-styleplugins](https://www.archlinux.org/packages/community/x86_64/qt5-styleplugins/).

## Installation

```bash
git clone https://github.com/GideonWolfe/Chameleon/
cd Chameleon
sudo ./install.sh
```

## Usage

* `chameleon -i [path to picture] [options for wal]`
* `chameleon -t [wal theme] [options for wal]`

## Configuration

Configuration of `chameleon` is done through the file `$HOME/.config/chameleon/config.yaml`

Here, one can specify options specific to a single program, or even specify custom commands to be run every time you apply a theme.

Most programs will have a `path` attribute which may or may not be necessary depending on your setup. For example, if you were using a cloned, local version of `wal-discord`, one
might want to specify a specific path where `chameleon` can find this specific executable.

If the `path` attribute is not given for a program, it is assumed that the program is located in your `$PATH` and will be run as a standalone command.

## Programs supported
* [oomox](https://github.com/themix-project/oomox) for GTK and Spotify

* [Zathura-Pywal](https://github.com/GideonWolfe/Zathura-Pywal)

* [Gnuplot-Pywal](https://github.com/GideonWolfe/Gnuplot-Pywal)

* [pyWalNeopixels](https://github.com/Paul-Houser/pyWalNeopixels)

* [slickgreeter-pywal](https://github.com/Paul-Houser/slickgreeter-pywal)

* [wal_steam](https://github.com/kotajacob/wal_steam) for steam: **NOTE**: Not guarunteed to work with steam library overhaul

* [ckb-next](https://github.com/ckb-next/ckb-next) for corsair keyboards

* [razer-cli](https://github.com/LoLei/razer-cli) for razer devices

* [telegram-palette-gen](https://github.com/matgua/telegram-palette-gen) for telegram-desktop

* [intelliJPywal](https://github.com/0x6C38/intellijPywal) for IntelliJ and other JetBrains IDEs (requires configuration in script)

* [Pywalfox](https://github.com/Frewacom/Pywalfox) to theme FireFox and DuckDuckGo on the fly

* [pywal-discord](https://github.com/FilipLitwora/pywal-discord) to theme Discord

* [wal-discord](https://github.com/guglicap/wal-discord) to theme Discord

## Planned support

## Notes
To get the most complete theme possible, check out my [dotfiles](https://github.com/GideonWolfe/PC-dotfiles). Here you can find the configurations to get these colors on many other programs, such as rofi, polybar, firefox, and more. Since they update automatically, there was no need to include them in this script.

To apply icon themes, you need one of the icon sets supported by oomox. Change the icons section of the script to look for the folder your desired icons are in, and change the command to the appropriate variant.

* [gnome-color-icons](https://aur.archlinux.org/packages/gnome-colors-icon-theme/)
* [archdroid icons](https://aur.archlinux.org/packages/archdroid-icon-theme/)
* [Materia icons](https://aur.archlinux.org/packages/materia-theme-git/)
