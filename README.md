# Chameleon

![alt-text](/demo.gif)

This script acts as an extension to wal, by taking the generated colors and theming anything that can be themed, all in one script.

If the script detects you have certain programs on your system, it will try to generate themes for them.

The current programs are ones that I use, but feel free to add more and send a PR!

# Examples

![alt-text](https://i.imgur.com/araXbD4.jpg)

Programs that use GTK themes like Thunar and Baobab should just pick up the theme, assuming you have selected the `oomox-xresources-reverse` theme in `lxappearance`. Spotify, Discord, Firefox, and gnuplot are shown here rocking their custom generated themes.

Programs that use Qt themes can also be configured to take themes from GTK, meaning we can theme them as well! The programs must be launched with the `--style gtk2` flag, and you must install and configure [qt5-styleplugins](https://www.archlinux.org/packages/community/x86_64/qt5-styleplugins/).

## Installation

```bash
git clone https://github.com/GideonWolfe/Chameleon/
cd Chameleon
make install
```

## Usage

* `chameleon -i [path to picture] [options for wal]`
* `chameleon -t [wal theme] [options for wal]`

## Configuration

Configuration of `chameleon` is done through the file `~/.config/chameleon/config.yaml`.

Here, one can specify options specific to a single program, or even specify custom commands to be run every time you apply a theme. Here's an example:

```yaml
xmenu:
  path: "~/.config/xmenu"
  command: "sudo make clean install"
  name: "XMenu"
```

As you can see, there're three parameters for each program:

1. **path**: The path to the required destination. For example, if you would like to run a program you wrote, you pass that directory to this parameter.
2. **command**: Obviously, this parameter is required for every program, if you want that program to be themed. If the command is a construction of multiple commands, you must break it up. For example:
```yaml
xmenu:
  path: "~/Desktop/Games/CPP/FirstPersonShooter"
  command:
    - "sudo make clean install"
    - "rm -rf build/"
    - "./open-window"
  name: "My Stupid Game"
```
3. **name**: The name of the program that you would like to be displayed if it was themed correctly/incorrectly.

As long as you pass the correct information, you can practically get any program to be themed.
