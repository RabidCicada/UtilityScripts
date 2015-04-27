from sys import argv
from subprocess import call
import re

funcmatcher = re.compile(r"^define.*@(.*)\(")
blockmatcher = re.compile(r"^(\S+):")
instmatcher = re.compile(r"^  [^ \t\n\r\f\v\]]\S*")
callmatcher = re.compile(r"^  (call|tail call).*%\S+\(")
#dstartblock = "block_0x807111f.i"
#dendblock = "block_0x807032b.i"
#debugmatcher = re.compile(r"^  (store|br|tail|unreachable|switch|call|ret|%\S+)\s")
#debugactive = False


def findtransition( callstr, tracefilename):
    with open(tracefilename, 'r') as tfile:

def processfiles( tracefilename, llvmfname, ofilename ):
    global debugactive
    #with open(callsfname, 'r') as callsfile,open(ofilename, 'w') as ofile:
        #for callstr in callsfile:
            #found = False
    currfunction = None
    block = None
    blockidx = 0
    funcidx = 0
    with open(llvmfname, 'r') as llvmfile,open(ofilename, 'w') as ofile, open("debugfile",'w') as dfile:
        for line in llvmfile:
            #Get rid of address numbers
            match  = funcmatcher.match(line)
            if match is not None:
                currfunction = match.group(1)
                funcidx = 0
                continue #get next line

            if currfunction is not None:
                #Get rid of offset labels
                match = blockmatcher.match(line)
                if match is not None:
                    #kill debugging if leaving last block of interest
                    #if dendblock == block:
                    #    debugactive = False
                    block = match.group(1)
                    blockidx=0
                    #enable debugging if entering first block of interest
                    #if dstartblock == block:
                    #    debugactive = True
                    continue
            
            if block is not None and instmatcher.match(line):
                if callmatcher.match(line) is not None:
                    dfile.write(line)
                #if debugactive:
                #    if debugmatcher.match(line) is None:
                #        dfile.write(line);
                #if line == callstr:
                    ofile.write(currfunction+"::"+block+"::" + str(funcidx) + "::" + str(blockidx) + "-->"+line)
                    findtransition( callstr, tracefilename):
                    #found = True
                    #break #found our string and have all info
                    continue
                blockidx+=1
                funcidx+=1
            else:
                pass
                #dfile.write(line);
    #if found!= True:
    #    ofile.write("Couldn't find owning func::block for callstr:" + callstr)
  
if __name__ == "__main__":
    processfiles(argv[1], argv[2])
