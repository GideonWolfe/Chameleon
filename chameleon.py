#!/usr/bin/env python3


import os
import yaml
import argparse
import subprocess
from os.path import expanduser


#  _   _ _   _ _ _ _   _
# | | | | |_(_) (_) |_(_) ___  ___
# | | | | __| | | | __| |/ _ \/ __|
# | |_| | |_| | | | |_| |  __/\__ \
#  \___/ \__|_|_|_|\__|_|\___||___/


class BColors:
    """Keeps all of the colors in one place."""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_status(status, program):
    """
    Prints the status of the program.
    0: Themed program,
    1: Failed to theme program,
    2: Warning,
    3: Hooked
    """

    end = BColors.ENDC
    fail = BColors.FAIL
    warning = BColors.WARNING
    green = BColors.OKGREEN
    blue = BColors.OKBLUE

    if status == 0:
        print(f"{green} ⚡ {end} Themed {program} {end}")
    elif status == 1:
        print(f"{fail} X {end} {warning} Failed to theme {program} {end}")
    elif status == 2:
        print(f"{fail} X {end} {warning} User Hook {program} failed {end}")
    elif status == 3:
        print(f"{green} ⚡ {end} {blue} {program} User hook {end} succeeded")


def run_command(commandlist, cwd=None, getoutput=None):
    stdout = subprocess.PIPE if getoutput else subprocess.DEVNULL

    p = subprocess.Popen(
        commandlist,
        cwd=cwd,
        stdout=stdout,
    )
    p.wait()

    return p.communicate()[0].decode("utf-8") if getoutput else ""


def get_info_for_item(config, item):
    cwd = config[item]["path"]
    exc = config[item]["executable"] or ""

    if exc != "":
        cmdList = (exc + " " + config[item]["arguments"]).split(" ")
    else:
        cmdList = config[item]["arguments"].split(" ")

    return cwd, exc, cmdList


#   ____             __ _
#  / ___|___  _ __  / _(_) __ _
# | |   / _ \| '_ \| |_| |/ _` |
# | |__| (_) | | | |  _| | (_| |
#  \____\___/|_| |_|_| |_|\__, |
#                         |___/

# get home directory
home = expanduser("~")

# get config path
config_dir = home + "/.config/chameleon"
config_path = home + "/.config/chameleon/config.yaml"

# store location of the scripts file
scripts_location = (
    f"{home}/.local/share/Singularis/third-party-tools" + "/chameleon/scripts"
)


# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="Chameleon Arguments",
        usage="%(prog)s -i/t [image/theme] [arguments for wal]",
    )
    parser.add_argument(
        "--theme",
        "-t",
        metavar="theme",
        type=str,
        nargs="?",
        help="a color scheme name to use as a theme",
    )
    parser.add_argument(
        "--image",
        "-i",
        metavar="image",
        type=str,
        nargs="?",
        help="an image file to use as a theme",
    )

    args = parser.parse_known_args()

    return args


# Parse user config file
def parse_yaml():
    with open(config_path, mode="r") as file:
        file_dict = yaml.full_load(file)
        file.close()
    return file_dict


# Print keys from a dictionary
def print_keys(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            print_keys(dictionary[key])


#  _____ _                    _
# |_   _| |__   ___ _ __ ___ (_)_ __   __ _
#   | | | '_ \ / _ \ '_ ` _ \| | '_ \ / _` |
#   | | | | | |  __/ | | | | | | | | | (_| |
#   |_| |_| |_|\___|_| |_| |_|_|_| |_|\__, |
#                                     |___/


def call_wal(args, walargs):
    # If we are calling wal on an image.
    if args.image:
        try:
            imagepath = os.path.abspath(args.image)
            commandlist = ["wal", "-i", imagepath]
            commandlist.extend(walargs)
            run_command(commandlist)
            run_command(["feh", "--bg-scale", args.image])
            run_command(["cp", args.image, "~/.config/wall.jpg"])
        except Exception:
            print_status(1, "pywal")
            return
    # If we are using a prebuilt or custom colorscheme.
    elif args.theme:
        try:
            commandlist = ["wal", "--theme", args.theme]
            commandlist.extend(walargs)
            run_command(commandlist)
        except Exception:
            print_status(1, "pywal")
            return
    print_status(0, "pywal")


def call_wal_discord(config):
    if "wal-discord" in config:
        try:
            cwd, _, cmdList = get_info_for_item(config, "wal-discord")
            run_command(cmdList, cwd=cwd)
        except Exception:
            print_status(1, "Discord")
            return
        print_status(0, "Discord")
    else:
        return


def call_xfce4(config):
    cwd = scripts_location

    if "xfce4-terminal" in config:
        try:
            path = config["xfce4-terminal"]["path"]

            xfce4_pywal = run_command(
                ["./xfce4-terminal.sh"],
                cwd=cwd,
                getoutput=True,
            )

            file = open(f"{path}/terminal/terminalrc", "w+")
            file.write(xfce4_pywal)
            file.close()
        except Exception:
            print_status(1, "Xfce4 Terminal")
            return
        print_status(0, "Xfce4 Terminal")
    else:
        return


def call_xmenu(config):
    if "xmenu" in config:
        try:
            cwd, _, cmdList = get_info_for_item(config, "xmenu")
            run_command(cmdList, cwd=cwd)
        except Exception:
            print_status(1, "Xmenu")
            return
        print_status(0, "Xmenu")
    else:
        return


def call_spicetify(config):
    name = "Spicetify"

    if "spicetify" in config:
        try:
            cwd, _, cmdList = get_info_for_item(config, "spicetify")
            run_command(cmdList, cwd=cwd)
        except Exception:
            print_status(1, name)
            return
    else:
        return
    print_status(0, name)


def call_oomoxicons(config):
    if "oomoxicons" in config:
        try:
            command = config["oomoxicons"]["command"]
            theme_path = config["oomoxicons"]["themepath"]
            p = subprocess.Popen(
                [command, theme_path],
                stdout=subprocess.DEVNULL,
            )
            p.wait()
        except Exception:
            print_status(1, "Oomox Icons")
            return
    print_status(0, "Oomox Icons")


def call_oomoxgtk(config):
    if "oomoxgtk" in config:
        try:
            theme_path = config["oomoxgtk"]["themepath"]
            p = subprocess.Popen(
                ["oomox-cli", theme_path],
                stdout=subprocess.DEVNULL,
            )
            p.wait()
        except Exception:
            print_status(1, "Oomox GTK")
            return
    print_status(0, "Oomox GTK")


def call_oomoxspotify(config):
    if "oomoxspotify" in config:
        if config["oomoxspotify"]["enabled"]:
            try:
                spotifypath = config["oomoxspotify"]["spotifypath"]
                full_command = (
                    f"oomoxify-cli {spotifypath}/.cache/wal/colors-oomox" "-s "
                )
                os.system(full_command)
            except Exception:
                print_status(1, "Oomox Spotify")
                return
            print_status(0, "Oomox Spofify")
        else:
            return
    else:
        return


def call_pywalfox(config):
    if "pywalfox" in config:
        try:
            if config["pywalfox"]["enable"]:
                p = subprocess.Popen(
                    ["pywalfox", "update"],
                    stdout=subprocess.DEVNULL,
                )
                p.wait()
            else:
                print_status(1, "Pywalfox")
                return
        except Exception:
            print_status(1, "Pywalfox")
            return
    print_status(0, "Pywalfox")


def call_starttree(config):
    if "starttree" in config:
        try:
            path = config["starttree"]["path"]
            p = subprocess.Popen(
                ["{}/generate.py".format(path)], stdout=subprocess.DEVNULL
            )
            p.wait()
        except Exception:
            print_status(1, "StartTree")
            return
    else:
        return
    print_status(0, "StartTree")


def theme(config, args, walargs):
    call_wal(args, walargs)
    # call_xfce4(config)
    call_wal_discord(config)
    call_xmenu(config)
    # call_oomoxicons(config)
    # call_oomoxgtk(config)
    # call_oomoxspotify(config)
    # call_pywalfox(config)
    # call_starttree(config)


def main():
    config = parse_yaml()
    args, walargs = parse_args()
    theme(config, args, walargs)


if __name__ == "__main__":
    main()
