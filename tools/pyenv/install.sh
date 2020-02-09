#!/usr/bin/env bash

SCRIPTDIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
ROOTDIR=../..
TOOLSDIR=$ROOTDIR/tools
$OS=${1:-ubuntu}

$OS/install.sh
