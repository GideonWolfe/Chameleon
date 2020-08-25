#!/bin/python3

import argparse
import yaml
import os
import subprocess
from os.path import expanduser
from shutil import copyfile
from bs4 import BeautifulSoup
from whichcraft import which
from shutil import which

#  _   _ _   _ _ _ _   _           
# | | | | |_(_) (_) |_(_) ___  ___ 
# | | | | __| | | | __| |/ _ \/ __|
# | |_| | |_| | | | |_| |  __/\__ \
#  \___/ \__|_|_|_|\__|_|\___||___/

def print_status(status, program):
    if(status == 0):
        print("⚡ Themed "+program)

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

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--theme', '-t', type=str, nargs='+', help='a color scheme name to use as a theme')
    parser.add_argument('--image', '-i', type=str, nargs='+', help='an image file to use as a theme')
    args = parser.parse_args()
    return args

def parse_yaml():
    with open(config_path, mode='r') as file:
        file_dict = yaml.full_load(file)
        file.close()
    return file_dict

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

def call_wal(args):
    # if we are calling wal on an image
    if(args.image):
        imagepath = os.path.abspath(args.image[0])
        commandstring = "wal -i "+imagepath
        print(commandstring)
        os.system(commandstring)
    # if we are using a prebuilt or custom colorscheme
    if(args.theme):
        commandstring = "wal --theme "+args.theme[0]
        os.system(commandstring)
    else:
        print("Error, missing required argument")


def call_slickpywal(config):
    # Check to see if the user defined a custom path
    if("slickpywal" in config):
        commandstring = config["slickpywal"]["path"]+"slick-pywal"
        os.system(commandstring)
    # Check to see if it exists somewhere in the path
    elif(is_tool("slick-pywal")):
        os.system("slick-pywal")
    else:
        return
    print("⚡ Themed Slick Greeter")
    return

def call_pywalneopixels(config):
    # Check to see if the user defined a custom path
    if("pywalneopixels" in config):
        commandstring = config["pywalneopixels"]["path"]+"startLEDs"
        os.system(commandstring)
    # Check to see if it exists somewhere in the path
    elif(is_tool("startLEDs")):
        os.system("startLEDs")
    else:
        return
    print_status(0, "Pywal NeoPixel")
    return


def call_wal_discord(config):
    # Check to see if the user defined a custom path
    if("waldiscord" in config):
        commandstring = config["waldiscord"]["path"]+"wal-discord -t"
        os.system(commandstring)
    # Check to see if it exists somewhere in the path
    elif(is_tool("wal-discord")):
        os.system("wal-discord -t")
    else:
        return
    print_status(0, "Discord")
    return

def call_xmenu(config):
    # Check to see if the user defined a custom path
    if("xmenu" in config):
        #  os.system(commandstring)
        p = subprocess.Popen(["make"], cwd=config["xmenu"]["path"])
        p.wait()
        p = subprocess.Popen(["sudo", "make", "install"], cwd=config["xmenu"]["path"])
        p.wait()
    # Check to see if it exists somewhere in the path
    else:
        return
    print_status(0, "Xmenu")
    return

def theme(config, args):
    #  call_wal(args)
    #  call_slickpywal(config)
    #  call_pywalneopixels(config)
    call_xmenu(config)

def main():
    config = parse_yaml()
    args = parse_args()
    theme(config, args)

if __name__ == '__main__':
    main()
