#!/usr/bin/env python3

import argparse
import yaml
import os
import subprocess
from os.path import expanduser
from shutil import copyfile
from whichcraft import which
from shutil import which

#  _   _ _   _ _ _ _   _
# | | | | |_(_) (_) |_(_) ___  ___
# | | | | __| | | | __| |/ _ \/ __|
# | |_| | |_| | | | |_| |  __/\__ \
#  \___/ \__|_|_|_|\__|_|\___||___/

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_status(status, program):
    if(status == 0):
        print(bcolors.OKGREEN + "⚡"+bcolors.ENDC+bcolors.OKBLUE+" Themed "+program + bcolors.ENDC)
    elif(status == 1):
        print(bcolors.FAIL + "X"+bcolors.ENDC+bcolors.WARNING+" Failed to theme "+program + bcolors.ENDC)
    elif(status == 2):
        print(bcolors.FAIL + "X"+bcolors.ENDC+bcolors.WARNING+" User hook "+program + " failed"+bcolors.ENDC)
    elif(status == 3):
        print(bcolors.OKGREEN + "⚡"+bcolors.ENDC+bcolors.OKBLUE+" User hook "+program + " succeeded"+bcolors.ENDC)

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

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Chameleon Arguments', usage='%(prog)s -i/t [image/theme] [arguments for wal]')
    parser.add_argument('--theme', '-t', metavar='theme', type=str, nargs='?', help='a color scheme name to use as a theme')
    parser.add_argument('--image', '-i', metavar='image', type=str, nargs='?', help='an image file to use as a theme')
    args = parser.parse_known_args()
    return args

# Parse user config file
def parse_yaml():
    with open(config_path, mode='r') as file:
        file_dict = yaml.full_load(file)
        file.close()
    return file_dict

# Print keys from a dictionary
def print_keys(dictionary):
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
    # if the user has defined hooks
    if("hooks" in config):
        # iterate through the hooks
        for value in config["hooks"].items():
            # If the user has a simple command to run
            if(type(value[1]) == str):
                #  print("single command found")
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
    # if we are calling wal on an image
    if(args.image):
        try:
            imagepath = os.path.abspath(args.image)
            commandlist = ["wal", "-i", imagepath]
            commandlist.extend(walargs)
            p = subprocess.Popen(commandlist)
            p.wait()
        except:
            print_status(1, "pywal")
            return
    # if we are using a prebuilt or custom colorscheme
    elif(args.theme):
        try:
            commandlist = ["wal", "--theme", args.theme]
            commandlist.extend(walargs)
            p = subprocess.Popen(commandlist)
            p.wait()
        except:
            print_status(1, "pywal")
            return
    print_status(0, "pywal")



def call_slickpywal(config):
    # Check to see if the user defined a custom path
    if("slickpywal" in config):
        try:
            p = subprocess.Popen(["slick-pywal"], cwd=config["slickpywal"]["path"])
            p.wait()
        except:
            print_status(1, "SlickGreeter Pywal")
            return
    # Check to see if it exists somewhere in the path
    elif(is_tool("slick-pywal")):
        try:
            p = subprocess.Popen(["slick-pywal"])
            p.wait()
        except:
            print_status(1, "SlickGreeter Pywal")
            return
    else:
        return
    print_status(0, "SlickGreeter Pywal")
    return

def call_pywalneopixels(config):
    # Check to see if the user defined a custom path
    if("pywalneopixels" in config):
        try:
            commandstring = config["pywalneopixels"]["path"]+"startLEDs"
            os.system(commandstring)
        except:
            print_status(1, "Pywal NeoPixel")
    # Check to see if it exists somewhere in the path
    elif(is_tool("startLEDS")):
        try:
            os.system("startLEDS")
        except:
            print_status(1, "Pywal NeoPixel")
            return
    # it is not detected it all
    else:
        return
    print_status(0, "Pywal NeoPixel")


def call_wal_discord(config):
    # Check to see if the user defined a custom path
    if("waldiscord" in config):
        try:
            m = subprocess.Popen(["wal-discord", "-t"], cwd=config["waldiscord"]["path"])
            m.wait()
        except:
            print_status(1, "Discord")
            return
        print_status(0, "Discord")
    # Check to see if it exists somewhere in the path
    elif(is_tool("wal-discord")):
        try:
            n = subprocess.Popen(["wal-discord", "-t"])
            n.wait()
        except:
            print_status(1, "Discord")
            return
        print_status(0, "Discord")
    else:
        return

def call_pywal_discord(config):
    # Check to see if the user defined a custom path
    if("pywaldiscord" in config):
        try:
            m = subprocess.Popen(["pywal-discord"], cwd=config["pywaldiscord"]["path"])
            m.wait()
        except:
            print_status(1, "Discord")
            return
        print_status(0, "Discord")
    # Check to see if it exists somewhere in the path
    elif(is_tool("pywal-discord")):
        try:
            n = subprocess.Popen(["pywal-discord"])
            n.wait()
        except:
            print_status(1, "Discord")
            return
        print_status(0, "Discord")
    else:
        return

def call_xmenu(config):
    # Check to see if the user defined a custom path
    if("xmenu" in config):
        try:
            # make xmenu
            null = open("/dev/null")
            m = subprocess.Popen(["make"], cwd=config["xmenu"]["path"], stdout=subprocess.DEVNULL)
            m.wait()
            retval = m.returncode
            null.close()
            # if making failed
            if(retval != 0):
                print_status(1, "Xmenu")
                return
            # Install the new files
            i = subprocess.Popen(["sudo", "make", "install"], cwd=config["xmenu"]["path"], stdout=subprocess.DEVNULL)
            i.wait()
            retval = m.returncode
            # if installation failed
            if(retval != 0):
                print_status(1, "Xmenu")
                return
        # If we found a config but something went wrong
        except:
            print_status(1, "Xmenu")
            return
        print_status(0, "Xmenu")
    # no config for xmenu, just return
    else:
        return

def call_cordless(config):
    if("cordless" in config):
        # the full path to the cordless theme template
        templatepath = config['cordless']['path']
        try:
            with open(home+"/.config/cordless/theme.json", "w") as theme:
                commandstring = "go run "+templatepath
                commandstring = commandstring.split(' ')
                g = subprocess.Popen(commandstring, stdout=theme)
                g.wait()
        except:
            print_status(1, "cordless")
            return
        print_status(0, "cordless")

def call_razercli(config):
    if("razercli" in config):
        try:
            p = subprocess.Popen([config['razercli']['path']+"razer-cli", '-a'])
            p.wait()
        except:
            print_status(1, "Razer Devices")
            return
    elif(is_tool("razer-cli")):
        try:
            p = subprocess.Popen(["razer-cli", "-a"])
            p.wait()
        except:
            print_status(1, "Razer Devices")
            return
    else:
        return
    print_status(0, "Razer Devices")

def call_spicetify(config):
    if("spicetify" in config):
        try:
            null = open("/dev/null")
            path = config['spicetify']['path']
            p = subprocess.Popen([path+"spicetify", 'update'], stdout=null)
            p.wait()
            null.close()
        except:
            print_status(1, "Spicetify")
            return
    elif(is_tool("spicetify")):
        try:
            null = open("/dev/null")
            p = subprocess.Popen(["spicetify", "apply"], stdout=null)
            p.wait()
            null.close()
        except:
            print_status(1, "Spicetify")
            return
    else:
        return
    print_status(0, "Spicetify")

def call_tellegrampallettegen(config):
    if("telegrampalletegen" in config):
        print("telegram was found in config")
        try:
            path = config['telegrampalletegen']['path']
            p = subprocess.Popen([path+"telegram-pallete-gen", '--wal'])
            p.wait()
        except:
            print_status(1, "Telegram Pallete")
            return
    elif(is_tool("telegram-palette-gen")):
        print("telegram was found to be tool")
        try:
            p = subprocess.Popen(["telegram-pallete-gen", "--wal"])
            p.wait()
        except:
            print_status(1, "Telegram Pallete")
            return
    else:
        return
    print_status(0, "Telegram Pallete")

def call_oomoxicons(config):
    if("oomoxicons" in config):
        try:
            command = config['oomoxicons']['command']
            themepath = config['oomoxicons']['themepath']
            fullcommand = command+" "+themepath+" > /dev/null"
            os.system(fullcommand)
        except:
            print_status(1, "Oomox Icons")
            return
    print_status(0, "Oomox Icons")

def call_oomoxgtk(config):
    if("oomoxgtk" in config):
        try:
            themepath = config['oomoxgtk']['themepath']
            fullcommand = "oomox-cli"+" "+themepath+" > /dev/null"
            os.system(fullcommand)
        except:
            print_status(1, "Oomox GTK")
            return
    print_status(0, "Oomox GTK")

#  Spicetify is preferred
def call_oomoxspotify(config):
    if("oomoxspotify" in config):
        if(config['oomoxspotify']['enabled'] == "True"):
            try:
                spotifypath = config['oomoxspotify']['spotifypath']
                fullcommand = "oomoxify-cli"+" "+home+"/.cache/wal/colors-oomox"+" -s "+spotifypath
                os.system(fullcommand)
            except:
                print_status(1, "Oomox Spotify")
                return
            print_status(0, "Oomox Spofify")
        else:
            return
    else:
        return

def call_pywalfox(config):
    if("pywalfox" in config):
        try:
            path = config['pywalfox']['path']
            p = subprocess.Popen([path+"pywalfox", 'update'])
            p.wait()
        except:
            print_status(1, "Pywalfox")
            return
    elif(is_tool("pywalfox")):
        try:
            p = subprocess.Popen(["pywalfox", "update"])
            p.wait()
        except:
            print_status(1, "Pywalfox")
            return
    print_status(0, "Pywalfox")

def call_gnuplot_pywal(config):
    if("gnuplotpywal" in config):
        try:
            path = config['gnuplotpywal']['path']
            file = open(home+"/.gnuplot", "w+")
            p = subprocess.Popen([path+"gengnuplotconfig"], stdout=file)
            p.wait()
            file.close()
        except:
            print_status(1, "Gnuplot")
            return
    elif(is_tool("gengnuplotconfig")):
        try:
            file = open(home+"/.gnuplot", "w+")
            p = subprocess.Popen(["gengnuplotconfig"], stdout=file)
            p.wait()
            file.close()
        except:
            print_status(1, "Gnuplot")
            return
    print_status(0, "Gnuplot")

def call_starttree(config):
    if("starttree" in config):
        try:
            path = config['starttree']['path']
            p = subprocess.Popen([path+"generate.py"])
            p.wait()
        except:
            print_status(1, "StartTree")
            return
    elif(is_tool("starttree.py")):
        try:
            p = subprocess.Popen(["starttree.py"], stdout=subprocess.DEVNULL)
            p.wait()
        except:
            print_status(1, "StartTree")
            return
    else:
        return
    print_status(0, "StartTree")

def theme(config, args, walargs):
    call_wal(args, walargs)
    call_slickpywal(config)
    call_pywalneopixels(config)
    call_wal_discord(config)
    call_xmenu(config)
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
