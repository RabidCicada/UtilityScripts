#!/usr/bin/env bash

# Call this script from anywhere you want.  It tracks the script's directory
SCRIPTDIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
ROOTDIR=..
TOOLSDIR=$ROOTDIR/tools
$OS=${1:-ubuntu}

# Copy in typical enhancements
cp $SCRIPTDIR/../bashrc ~/.bashrc.custom
if grep -q ".pyenv.bashrc" $BASHFILE
  echo "[ -f $HOME/.pyenv.bashrc ] && source $HOME/.pyenv.bashrc" >> $BASHFILE
  ####
fi

# Install pyenv
$TOOLSDIR/pyenv/install_pyenv_for_ubuntu.sh

# Copy in Tmux config
cp $TOOLSDIR/tmux/.tmux.conf.linux $HOME/.tmux.conf

# Copy in git config
cp $TOOLSDIR/git/.gitconfig $HOME/.gitconfig

# Install Atom and packages
$TOOLSDIR/atom/$OS/install_atom.sh
apm install --packages-file $TOOLSDIR/atom/packages.txt
