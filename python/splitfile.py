#!/usr/bin/python
#This script is used to split a file on a string match and create sequential
#output files with a common prefix

from sys import argv
from subprocess import call
import re

def debugHook(line):
    print line + "\n"
    debugHook.cnt+=1
    if debugHook.cnt > 5:
        raise SystemExit
debugHook.cnt=0

def processfiles( ifilename, splitmatch, ofilenameprefix ):
    idx = 0
    debugcnt=0

    if ofilenameprefix=="":
        ofilenameprefix = ifilename+".split."

    print "InputFile: " + ifilename
    print "SplitMatch: \"" + splitmatch + "\""
    print "OutputPrefix: " + ofilenameprefix

    with open(ifilename, 'r') as ifile:
        ofile =  open(ofilenameprefix + str(idx) + ".txt", 'w')
        for line in ifile:

            #Check for match and split file if match
            if(line.strip() == splitmatch.strip()):
                ofile.close()
                idx+=1
                ofile =  open(ofilenameprefix + str(idx) + ".txt", 'w')

            #debugHook(line+splitmatch)

            #Get rid of offset labels
            ofile.write(line)

def printUsage():
    print "Usage: " + argv[0] + " <inputfile> <splitmatch> [outputfileprefix]"
    print "This program will take an input file and split it into multiple"
    print "sequential files by splitting the contents on the matching string"

if __name__ == "__main__":
    if len(argv) >=3:
        if len(argv) < 4:
            processfiles(argv[1], argv[2], "")
        else:
            processfiles(argv[1],argv[2],argv[3])
    else:
        printUsage()
