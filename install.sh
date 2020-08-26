#!/bin/bash
FILEPATH=$(readlink -f "chameleon.py")
ln -s $FILEPATH $HOME/.local/bin/chameleon.py
echo "chameleon.py has been linked to $HOME/.local/bin/"
echo "Ensure this directory is in your \$PATH"

echo "Downloading pip dependencies"
pip install --user whichcraft
