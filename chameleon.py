#!/usr/bin/env python3


import os
import argparse
import subprocess
from os.path import expanduser
from utils import print_status as print_status
from utils import run_command as run_command
from utils import get_info_for_item as get_info_for_item
from utils import parse_yaml


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


def theme_program(config, name, program_name):
    if name not in config:
        return

    try:
        cwd, _, _, cmdList = get_info_for_item(config, name)
        run_command(cmdList, cwd=cwd)
    except Exception:
        print_status(1, program_name)
        return

    print_status(0, program_name)


def call_xfce4(config):
    if "xfce4-terminal" not in config:
        return

    name = "Xfce4 Terminal"
    try:
        cwd, config_path, _, cmdList = get_info_for_item(
            config,
            "xfce4-terminal",
        )

        xfce4_pywal = run_command(
            cmdList,
            cwd=cwd,
            getoutput=True,
        )

        file = open(config_path, "w+")
        file.write(xfce4_pywal)
        file.close()
    except Exception:
        print_status(1, name)
        return

    print_status(0, name)


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
    call_xfce4(config)
    theme_program(config, "wal-discord", "Discord")
    theme_program(config, "xmenu", "XMenu")
    theme_program(config, "oomoxicons", "Oomox Icons")
    theme_program(config, "oomoxgtk", "Oomox GTK")
    theme_program(config, "oomoxspotify", "Spotify")
    theme_program(config, "pywalfox", "Pywal Fox")
    theme_program(config, "starttree", "Start Tree")


def main():
    config = parse_yaml(config_path)
    args, walargs = parse_args()
    theme(config, args, walargs)


if __name__ == "__main__":
    main()
