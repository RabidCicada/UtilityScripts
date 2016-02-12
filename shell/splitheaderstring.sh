#!bin/bash
#This requires a specially created version of fold that supports the -d<char>
#option (avoid breaking on character) it was created by kyle stapp to facilitate
# easy header file style split strings with fold and lives here
#https://github.com/RabidCicada/coreutils

#It turns a normal xml document into something like below so that it can be read
# and parsed inline as an xml document from withing a C++ file
# This is how lightdm-gtk provides default look and feel to their dm

# "<xml><field attribute=\"derp\"><more-nested-shit>words</more-nested-shit></f"
# "ield></xml>"
sed 's/^[[:space:]]*//' $1 | sed 's/[[:space:]]*$//' | sed -z 's/\n//g' | sed 's/"/\\"/g' | fold -w76 -d\\ |  sed 's/^/  "/g' | sed 's/$/"/g' > $2
