#!/usr/bin/env bash

# Call this function from anywhere you want.  It tracks the script's directory
SCRIPTDIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))

wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
sudo apt update
sudo apt install atom
