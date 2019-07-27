# autoTheme

This script acts as an extension to wal, by taking the generated colors and theming anything that can be themed, all in one script. 

If the script detects you have certain programs on your system, it will try to generate themes for them.

The current programs are ones that I use, but feel free to add more and send a PR!

## Usage

`theme [path to picture] [options for wal]`

There are so many programs called from this script, it is easier to just edit the script to change the flags to your liking. for example, `wal_steam` is set to always use the `-w` option to take colors from wal. If you would rather use `-w` for a wpgtk theme, just change it in the script.

## Programs supported
[oomox](https://github.com/themix-project/oomox) for GTK and Spotify

[Zathura-Pywal](https://github.com/GideonWolfe/Zathura-Pywal)

[Gnuplot-Pywal](https://github.com/GideonWolfe/Gnuplot-Pywal)

[wal_steam](https://github.com/kotajacob/wal_steam) for steam

[ckb-next](https://github.com/ckb-next/ckb-next) for corsair keyboards

[telegram-palette-gen](https://github.com/matgua/telegram-palette-gen) for telegram-desktop

## Planned support
DuckDuckGo search colors
