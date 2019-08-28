


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
   ________                         __               
   / ____/ /_  ____ _____ ___  ___  / /__  ____  ____ 
  / /   / __ \/ __  / __  __ \/ _ \/ / _ \/ __ \/ __ \ 
 / /___/ / / / /_/ / / / / / /  __/ /  __/ /_/ / / / / 
 \____/_/ /_/\__,_/_/ /_/ /_/\___/_/\___/\____/_/ /_/ 


![alt text](https://media.giphy.com/media/WRXd64lryjPN4Rkj9K/giphy.gif)

=======

This script acts as an extension to wal, by taking the generated colors and theming anything that can be themed, all in one script. 

If the script detects you have certain programs on your system, it will try to generate themes for them.

The current programs are ones that I use, but feel free to add more and send a PR!

## Installation

```bash
git clone https://github.com/GideonWolfe/Chameleon/
cd Chameleon
sudo ./install.sh
```

## Usage

`theme [path to picture] [options for wal]`

There are so many programs called from this script, it is easier to just edit the script to change the flags to your liking. for example, `wal_steam` is set to always use the `-w` option to take colors from wal. If you would rather use `-g` for a wpgtk theme, just change it in the script.

## Programs supported
* [oomox](https://github.com/themix-project/oomox) for GTK and Spotify

* [Zathura-Pywal](https://github.com/GideonWolfe/Zathura-Pywal)

* [Gnuplot-Pywal](https://github.com/GideonWolfe/Gnuplot-Pywal)

* [wal_steam](https://github.com/kotajacob/wal_steam) for steam

* [ckb-next](https://github.com/ckb-next/ckb-next) for corsair keyboards

* [telegram-palette-gen](https://github.com/matgua/telegram-palette-gen) for telegram-desktop

* [intelliJPywal](https://github.com/0x6C38/intellijPywal) for IntelliJ and other JetBrains IDEs (requires configuration in script)

## Planned support
* DuckDuckGo search colors
* Discord (wal-discord seems broken for me)
* razer keyboards with [openrazer_pywal](https://github.com/bisspector/openrazer_pywal). I don't have a razer keyboard to test.

## Notes
To get the most complete theme possible, check out my [dotfiles](https://github.com/GideonWolfe/PC-dotfiles). Here you can find the configurations to get these colors on many other programs, such as rofi, polybar, firefox, and more. Since they update automatically, there was no need to include them in this script.

To apply icon themes, you need one of the icon sets supported by oomox. Change the icons section of the script to look for the folder your desired icons are in, and change the command to the appropriate variant.

* [gnome-color-icons](https://aur.archlinux.org/packages/gnome-colors-icon-theme/)
* [archdroid icons](https://aur.archlinux.org/packages/archdroid-icon-theme/)
* [Materia icons](https://aur.archlinux.org/packages/materia-theme-git/)
