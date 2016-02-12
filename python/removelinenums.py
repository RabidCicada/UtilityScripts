#!/bin/python
#Removes simple line numbers from a file
#Uses include removing numbering to allow more accuret compare vs another text
#file

from sys import argv
from subprocess import call
import re

dissasmsuffix = ".diss.txt"
strippedsuffix = ".stripped"

def processfiles( ifilename, ofilename ):
    with open(ifilename, 'r'),open(ofilename, 'w') as ifile,ofile:
    for line in f:
        #Get rid of address numbers
        line = re.sub(r"^[0-9a-z]{8}:*s","")
        #Get rid of offset labels
        line.replace("<.*>$","")
        ofile.write(line)


if __name__ == "__main__":
    processfiles(argv[1], argv[2])
