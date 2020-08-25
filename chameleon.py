#!/bin/python3

import argparse
import yaml
import os
from os.path import expanduser
from shutil import copyfile
from bs4 import BeautifulSoup

# get home directory
home = expanduser("~")

# get config path
config_dir = home + '/.config/chameleon'
config_path = home + '/.config/chameleon/config.yaml'

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--scheme', '-s', type=str, nargs='+', help='a color scheme name to use as a theme')
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

def call_wal(args):
    imagepath = os.path.abspath()
    commandstring = "wal -i " + imagepath

def main():
    #  file_dict = parse_yaml()
    #  print_keys(file_dict)
    args = parse_args()
    print(args)

if __name__ == '__main__':
    main()
