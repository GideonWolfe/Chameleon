#!/usr/bin/env python3


import os
import argparse
import subprocess
from os.path import expanduser
from whichcraft import which
import yaml


#  _   _ _   _ _ _ _   _
# | | | | |_(_) (_) |_(_) ___  ___
# | | | | __| | | | __| |/ _ \/ __|
# | |_| | |_| | | | |_| |  __/\__ \
#  \___/ \__|_|_|_|\__|_|\___||___/

class BColors:
    """
    Keeps all of the colors in one place.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_status(status, program):
    """
    Prints the status of the program.
    0: Themed program,
    1: Failed to theme program,
    2: Warning,
    3: Hooked
    """
    if status == 0:
        print('{} ⚡ {} Themed {} {}'.format(
            BColors.OKGREEN,
            BColors.ENDC,
            program,
            BColors.ENDC
        ))
    elif status == 1:
        print('{} X {} {} Failed to theme {} {}'.format(
            BColors.FAIL,
            BColors.ENDC,
            BColors.WARNING,
            BColors.ENDC
        ))
    elif status == 2:
        print('{} X {} {} User Hook {} failed {}'.format(
              BColors.FAIL,
              BColors.ENDC,
              BColors.WARNING,
              program,
              BColors.ENDC
              ))
    elif status == 3:
        print('{} ⚡ {} {} User hook {} succeeded'.format(
            BColors.OKGREEN,
            BColors.ENDC,
            BColors.OKBLUE,
            program,
            BColors.ENDC
        ))


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None


#   ____             __ _
#  / ___|___  _ __  / _(_) __ _
# | |   / _ \| '_ \| |_| |/ _` |
# | |__| (_) | | | |  _| | (_| |
#  \____\___/|_| |_|_| |_|\__, |
#                         |___/

# get home directory
home = expanduser("~")

# get config path
config_dir = home + '/.config/chameleon'
config_path = home + '/.config/chameleon/config.yaml'

# store location of the scripts file
scripts_location = home + '/Singularis/third-party-tools/chameleon/scripts'


# Parse command line arguments
def parse_args():
    """
    This function goes through all of the arguments using argparse.
    """
    parser = argparse.ArgumentParser(
        description='Chameleon Arguments',
        usage='%(prog)s -i/t [image/theme] [arguments for wal]')
    parser.add_argument('--theme',
                        '-t',
                        metavar='theme',
                        type=str, nargs='?',
                        help='a color scheme name to use as a theme')
    parser.add_argument('--image',
                        '-i',
                        metavar='image',
                        type=str, nargs='?',
                        help='an image file to use as a theme')

    args = parser.parse_known_args()

    return args


# Parse user config file
def parse_yaml():
    """
    This function parses through the config.yaml file.
    """
    with open(config_path, mode='r') as file:
        file_dict = yaml.full_load(file)
        file.close()
    return file_dict


# Print keys from a dictionary
def print_keys(dictionary):
    """
    This function stores all of the keys in a dictionary.
    """
    for key in dictionary:
        print(key)
        if isinstance(dictionary[key], dict):
            print_keys(dictionary[key])


#  _____ _                    _
# |_   _| |__   ___ _ __ ___ (_)_ __   __ _
#   | | | '_ \ / _ \ '_ ` _ \| | '_ \ / _` |
#   | | | | | |  __/ | | | | | | | | | (_| |
#   |_| |_| |_|\___|_| |_| |_|_|_| |_|\__, |
#                                     |___/

# Detects and runs hooks set by user
def user_hooks(config):
    """
    Runs user hooks.
    """
    # If the user has defined hooks
    if 'hooks' in config:
        # Iterate through the hooks
        for value in config['hooks'].items():
            # If the user has a simple command to run
            if type(value[1]) == str:
                try:
                    arglist = value[1].split(' ')
                    p = subprocess.Popen(arglist)
                    p.wait()
                except:
                    print_status(2, value[0])
                    return
            # User has specified options for the hook
            elif(type(value[1]) == dict):
                path = value[1].get('directory', './')
                arglist = value[1].get('command').split(' ')
                try:
                    p = subprocess.Popen(arglist, cwd=path)
                    p.wait()
                except:
                    print_status(2, value[0])
                    return
            print_status(3, value[0])


def call_wal(args, walargs):
    """
    Runs wal.
    """
    # If we are calling wal on an image
    if args.image:
        try:
            imagepath = os.path.abspath(args.image)
            commandlist = ['wal', '-i', imagepath]
            commandlist.extend(walargs)
            p = subprocess.Popen(commandlist)
            p.wait()
            os.system('feh --bg-scale {} && cp {} ~/.config/wall.jpg'.format(args.image, args.image))
        except:
            print_status(1, 'pywal')
            return
    # If we are using a prebuilt or custom colorscheme
    elif args.theme:
        try:
            commandlist = ['wal', '--theme', args.theme]
            commandlist.extend(walargs)
            p = subprocess.Popen(commandlist)
            p.wait()
        except:
            print_status(1, 'pywal')
            return
    print_status(0, 'pywal')


def call_slickpywal(config):
    """
    Changes the theme for slickpywal.
    """
    # Check to see if the user defined a custom path
    if 'slickpywal' in config:
        try:
            p = subprocess.Popen(['slick-pywal'], cwd=config['slickpywal']['path'])
            p.wait()
        except:
            print_status(1, 'SlickGreeter Pywal')
            return
    # Check to see if it exists somewhere in the path
    elif is_tool('slick-pywal'):
        try:
            p = subprocess.Popen(['slick-pywal'])
            p.wait()
        except:
            print_status(1, 'SlickGreeter Pywal')
            return
    else:
        return
    print_status(0, 'SlickGreeter Pywal')
    return


def call_pywalneopixels(config):
    """
    Changes the theme for pywalneopixels.
    """
    # Check to see if the user defined a custom path
    if 'pywalneopixels' in config:
        try:
            command_string = '{}startLEDs'.format(
                config['pywalneopixels']['path'])
            os.system(command_string)
        except:
            print_status(1, 'Pywal NeoPixel')
    # Check to see if it exists somewhere in the path
    elif is_tool('startLEDS'):
        try:
            os.system('startLEDS')
        except:
            print_status(1, 'Pywal NeoPixel')
            return
    # It is not detected it all
    else:
        return
    print_status(0, 'Pywal NeoPixel')


def call_wal_discord(config):
    """
    Changes the theme for discord.
    """
    # Check to see if the user defined a custom path
    if 'waldiscord' in config:
        try:
            m = subprocess.Popen(['wal-discord', '-t'],
                                 cwd=config['waldiscord']['path'])
            m.wait()
        except:
            print_status(1, 'Discord')
            return
        print_status(0, 'Discord')
    # Check to see if it exists somewhere in the path
    elif is_tool('wal-discord'):
        try:
            n = subprocess.Popen(['wal-discord', '-t'])
            n.wait()
        except:
            print_status(1, 'Discord')
            return
        print_status(0, 'Discord')
    else:
        return


def call_pywal_discord(config):
    # Check to see if the user defined a custom path
    if "pywaldiscord" in config:
        try:
            m = subprocess.Popen ["pywal-discord"], \
                cwd=config['pywaldiscord']['path']
            m.wait()
        except:
            print_status(1, 'Discord')
            return
        print_status(0, 'Discord')
    # Check to see if it exists somewhere in the path
    elif(is_tool('pywal-discord')):
        try:
            n = subprocess.Popen(['pywal-discord'])
            n.wait()
        except:
            print_status(1, 'Discord')
            return
        print_status(0, 'Discord')
    else:
        return

def call_dunst(config):
    # Check to see if the user defined a custom path
    if 'dunst' in config:
        try:
            # Run the theme file
            dunst_pywal = subprocess.getoutput('{}/dunst.sh'.format(scripts_location))
            # Open file
            file = open('{}/dunstrc'.format(config['dunst']['path']), 'w+')
            file.write(dunst_pywal)
            file.close()
        # If we found a config but something went wrong
        except:
            print_status(1, "Dunst")
            return
        print_status(0, "Dunst")
    # no config for dunst, just return
    else:
        return

def call_xmenu(config):
    # Check to see if the user defined a custom path
    if 'xmenu' in config:
        try:
            if 'xmenu-pywal' in config:
                # Run the theme file
                xmenu_pywal = subprocess.getoutput('{}/xmenu.sh'.format(
                    config['scripts_location']['path']))
                # Open file
                file = open('{}/colors-xmenu.h'.format(
                    config['xmenu']['path']), 'w+')
                file.write(xmenu_pywal)
                file.close()

            # Make xmenu
            null = open('/dev/null')
            m = subprocess.Popen(['make'], cwd=config['xmenu']['path'],
                                 stdout=subprocess.DEVNULL)
            m.wait()
            retval = m.returncode
            null.close()
            # If making failed
            if retval != 0:
                print_status(1, 'Xmenu')
                return
            # Install the new files
            i = subprocess.Popen(['sudo', 'make', 'install'],
                                 cwd=config['xmenu']['path'],
                                 stdout=subprocess.DEVNULL)
            i.wait()
            retval = m.returncode
            # If installation failed
            if retval != 0:
                print_status(1, 'Xmenu')
                return

        # If we found a config but something went wrong
        except:
            print_status(1, 'Xmenu')
            return
        print_status(0, 'Xmenu')
    # No config for xmenu, just return
    else:
        return


def call_dwm(config):
    # Check to see if the user defined a custom path
    if 'dwm' in config:
        try:
            # Make dwm
            null = open('/dev/null')
            m = subprocess.Popen(['make'], cwd=config['dwm']['path'],
                                 stdout=subprocess.DEVNULL)
            m.wait()
            retval = m.returncode
            null.close()
            # If making failed
            if(retval != 0):
                print_status(1, 'Dwm')
                return
            # Install the new files
            i = subprocess.Popen(['sudo', 'make', 'clean', 'install'],
                                 cwd=config['dwm']['path'],
                                 stdout=subprocess.DEVNULL)
            i.wait()
            retval = m.returncode
            # If installation failed
            if retval != 0:
                print_status(1, 'Dwm')
                return
        # If we found a config but something went wrong
        except:
            print_status(1, 'Dwm')
            return
        print_status(0, 'Dwm')
    # No config for dwm, just return
    else:
        return


def call_zathura(config):
    # Check to see if the user defined a custom path
    if 'zathura' in config:
        try:
            # Run the theme file
            zathura_pywal = subprocess.getoutput('{}/zathura.sh'.format(scripts_location))
            # Open file
            file = open('{}/zathurarc'.format(config['zathura']['path']), 'w+')
            file.write(zathura_pywal)
            file.close()
        # If we found a config but something went wrong
        except:
            print_status(1, "Zathura")
            return
        print_status(0, "Zathura")
    # no config for zathura, just return
    else:
        return

def call_matplotlib(config):
    # Check to see if the user defined a custom path
    if 'matplotlib' in config:
        try:
            # Run the theme file
            matplotlib_pywal = subprocess.getoutput('{}/matplotlib.sh'.format(scripts_location))
            # Open file
            file = open('{}/matplotlibrc'.format(config['matplotlib']['path']), 'w+')
            file.write(matplotlib_pywal)
            file.close()
        # If we found a config but something went wrong
        except:
            print_status(1, "Matplotlib")
            return
        print_status(0, "Matplotlib")
    # no config for matplotlib, just return
    else:
        return

def call_xfce4(config):
    # Check to see if the user defined a custom path
    if 'xfce4-terminal' in config:
        try:
            # Run the theme file
            xfce4_pywal = subprocess.getoutput('{}/xfce4-terminal.sh'.format(scripts_location))
            # Open file
            file = open('{}/terminal/terminalrc'.format(config['xfce4-terminal']['path']), 'w+')
            file.write(xfce4_pywal)
            file.close()
        # If we found a config but something went wrong
        except:
            print_status(1, 'Xfce4 Terminal')
            return
        print_status(0, 'Xfce4 Terminal')
    # No config for xfce4-terminal, just return
    else:
        return


def call_cordless(config):
    if 'cordless' in config:
        # The full path to the cordless theme template
        templatepath = config['cordless']['path']
        try:
            with open('{}/.config/cordless/theme.json'.format(home),
                      "w") as theme:
                command_string = 'go run {}'.format(templatepath)
                command_string = command_string.split(' ')
                g = subprocess.Popen(commandstring, stdout=theme)
                g.wait()
        except:
            print_status(1, 'cordless')
            return
        print_status(0, 'cordless')


def call_razercli(config):
    if 'razercli' in config:
        try:
            p = subprocess.Popen([config['razercli']['path']+'razer-cli', '-a'])
            p.wait()
        except:
            print_status(1, 'Razer Devices')
            return
    elif is_tool('razer-cli'):
        try:
            p = subprocess.Popen(['razer-cli', '-a'])
            p.wait()
        except:
            print_status(1, 'Razer Devices')
            return
    else:
        return
    print_status(0, 'Razer Devices')


def call_spicetify(config):
    if 'spicetify' in config:
        try:
            null = open('/dev/null')
            path = config['spicetify']['path']
            p = subprocess.Popen(['{}spicetify'.format(path), 'update'],
                                 stdout=null)
            p.wait()
            null.close()
        except:
            print_status(1, 'Spicetify')
            return
    elif is_tool('spicetify'):
        try:
            null = open('/dev/null')
            p = subprocess.Popen(['spicetify', 'apply'], stdout=null)
            p.wait()
            null.close()
        except:
            print_status(1, 'Spicetify')
            return
    else:
        return
    print_status(0, 'Spicetify')


def call_tellegrampallettegen(config):
    if "telegrampalletegen" in config:
        print('telegram was found in config')
        try:
            path = config['telegrampalletegen']['path']
            p = subprocess.Popen(['{}telegram-pallete-gen'.format(path),
                                  '--wal'])
            p.wait()
        except:
            print_status(1, 'Telegram Pallete')
            return
    elif is_tool('telegram-palette-gen'):
        print('telegram was found to be tool')
        try:
            p = subprocess.Popen(['telegram-pallete-gen', '--wal'])
            p.wait()
        except:
            print_status(1, 'Telegram Pallete')
            return
    else:
        return
    print_status(0, 'Telegram Pallete')


def call_oomoxicons(config):
    if "oomoxicons" in config:
        try:
            command = config['oomoxicons']['command']
            theme_path = config['oomoxicons']['themepath']
            full_command = '{} {} > /dev/null'.format(command, theme_path)
            os.system(full_command)
        except:
            print_status(1, 'Oomox Icons')
            return
    print_status(0, 'Oomox Icons')


def call_oomoxgtk(config):
    if 'oomoxgtk' in config:
        try:
            os.system('rm -rf ~/.themes/oomox-xresources-reverse/')
            os.system('rm -rf ~/.icons/oomox-xresources-reverse/')
            theme_path = config['oomoxgtk']['themepath']
            full_command = 'oomox-cli {} > /dev/null'.format(theme_path)
            os.system(full_command)
        except:
            print_status(1, 'Oomox GTK')
            return
    print_status(0, 'Oomox GTK')


# Spicetify is preferred
def call_oomoxspotify(config):
    if 'oomoxspotify' in config:
        if config['oomoxspotify']['enabled']:
            try:
                spotifypath = config['oomoxspotify']['spotifypath']
                full_command = 'oomoxify-cli {}/.cache/wal/colors-oomox' \
                    '-s '.format(home, spotifypath)
                os.system(full_command)
            except:
                print_status(1, 'Oomox Spotify')
                return
            print_status(0, 'Oomox Spofify')
        else:
            return
    else:
        return


def call_pywalfox(config):
    if 'pywalfox' in config:
        try:
            path = config['pywalfox']['path']
            p = subprocess.Popen(['{}pywalfox'.format(path), 'update'])
            p.wait()
        except:
            print_status(1, 'Pywalfox')
            return
    elif is_tool('pywalfox'):
        try:
            p = subprocess.Popen(['pywalfox', 'update'])
            p.wait()
        except:
            print_status(1, 'Pywalfox')
            return
    print_status(0, 'Pywalfox')


def call_gnuplot_pywal(config):
    if 'gnuplotpywal' in config:
        try:
            path = config['gnuplotpywal']['path']
            file = open('{}/.gnuplot'.format(home), 'w+')
            p = subprocess.Popen(['{}gengnuplotconfig'.format(path)], stdout=file)
            p.wait()
            file.close()
        except:
            path = config['gnuplotpywal']['path']
            print(path)
            print_status(1, 'Gnuplot')
            return
    elif is_tool('gengnuplotconfig'):
        try:
            file = open('{}/.gnuplot'.format(home), 'w+')
            p = subprocess.Popen(['gengnuplotconfig'], stdout=file)
            p.wait()
            file.close()
        except:
            print_status(1, 'Gnuplot')
            return
    print_status(0, 'Gnuplot')


def call_starttree(config):
    if "starttree" in config:
        try:
            path = config['starttree']['path']
            p = subprocess.Popen(['{}/generate.py'.format(path)])
            p.wait()
        except:
            print_status(1, 'StartTree')
            return
    elif is_tool('starttree.py'):
        try:
            p = subprocess.Popen(['starttree.py'], stdout=subprocess.DEVNULL)
            p.wait()
        except:
            print_status(1, 'StartTree')
            return
    else:
        return
    print_status(0, 'StartTree')


def theme(config, args, walargs):
    call_wal(args, walargs)
    call_slickpywal(config)
    call_pywalneopixels(config)
    call_wal_discord(config)
    call_xmenu(config)
    call_dwm(config)
    call_zathura(config)
    call_matplotlib(config)
    call_xfce4(config)
    call_dunst(config)
    call_cordless(config)
    call_razercli(config)
    call_spicetify(config)
    call_tellegrampallettegen(config)
    call_oomoxicons(config)
    call_oomoxgtk(config)
    call_oomoxspotify(config)
    call_pywalfox(config)
    call_gnuplot_pywal(config)
    call_starttree(config)
    user_hooks(config)


def main():
    config = parse_yaml()
    args, walargs = parse_args()
    theme(config, args, walargs)


if __name__ == '__main__':
    main()

