#!/usr/bin/env bash

# Call this function from anywhere you want.  It tracks the script's directory
SCRIPTDIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
BASHFILE=$HOME/.bashrc
PYENVBASHRC=.bashrc.pyenv

#Install pyenv and configure
cp $SCRIPTDIR/bashrc.pyenv ~/$PYENVBASHRC
if grep -q "$PYENVBASHRC" $BASHFILE
  echo "[ -f $HOME/$PYENVBASHRC ] && source $HOME/$PYENVBASHRC" >> $BASHFILE
fi
source $BASHFILE
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

pyenv install 3.8.1
pyenv virtualenv 3.8.1 dev
