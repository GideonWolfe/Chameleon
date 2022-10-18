import yaml
import subprocess
import os


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
    cwd = ""
    config_path = ""
    exc = ""
    cmdList = ""

    try:
        cwd = config[item]["path"]
    except Exception:
        cwd = os.getenv("HOME")

    try:
        config_path = config[item]["config_path"]
    except Exception:
        config_path = ""

    try:
        exc = config[item]["executable"]
    except Exception:
        exc = ""

    try:
        if exc != "":
            cmdList = (exc + " " + config[item]["arguments"]).split(" ")
        else:
            cmdList = config[item]["arguments"].split(" ")
    except Exception:
        if exc != "":
            cmdList = exc

    return cwd, config_path, exc, cmdList


def parse_yaml(config_path):
    with open(config_path, mode="r") as file:
        file_dict = yaml.full_load(file)
        file.close()
    return file_dict
