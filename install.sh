#!/usr/bin/env bash
FILEPATH=$(readlink -f "chameleon.py")
ln -sf $FILEPATH $HOME/.local/bin/chameleon.py
echo "chameleon.py has been linked to $HOME/.local/bin/"
echo "Ensure this directory is in your \$PATH"
type pip > /dev/null 2>&1 || Pip_ver="pip3"
echo "Downloading ${Pip_ver:-pip} dependencies"
$Pip_ver install --user whichcraft
