

#!/bin/python
#This script is to specific to be useful in general in current form but the idea
#was that it is a multi state matching pile of junk that can match a particular
#transition in a file.


from sys import argv
from subprocess import call
import re

funcmatcher = re.compile(r"^define.*@(.*)\(")
blockmatcher = re.compile(r"^(\S+):")
traceblockmatcher = re.compile(r"^        \"([a-zA-Z_0-9]+)\.(\S+).*\.inst_[a-zA-Z_x0-9]+\",")
traceaddrmatcher = re.compile(r"^        \"(0x[a-zA-Z0-9]+)\",")
instmatcher = re.compile(r"^  [^ \t\n\r\f\v\]]\S*")
callmatcher = re.compile(r"^  (call|tail call).*%\S+\(")
#dstartblock = "block_0x807111f.i"
#dendblock = "block_0x807032b.i"
#debugmatcher = re.compile(r"^  (store|br|tail|unreachable|switch|call|ret|%\S+)\s")
#debugactive = False


def findtransitions( tgtfunc, tgtblock, callstr, tracefilename):
	currfunc = None
	currblock = None
	nextcall = None
	nextblock = None
	address = None
	lineidx = 1
	transitions = []
        print "Investigating for " + callstr + "<" + tgtfunc + "," + tgtblock + ">"
	with open(tracefilename, 'r') as tfile:
		for line in tfile:
			match = traceblockmatcher.match(line)
			if match is not None:
                                #print "found func.block name " + line 
				nextfunc = match.group(1)
				nextblock = match.group(2)
				address = None
			else:
                                #print "nonmatching " + line
                                match = traceaddrmatcher.match(line)
                                if match is not None:
                                        address = match.group(1)
                                else:
                                        address = None
				nextfunc = None
				nextblock = None

			if nextfunc is not None and nextfunc != currfunc:
                                #print "Checking " + str(nextfunc) + "." + str(nextblock) + " === " + line
				#start once we found a likely callsite
				if nextfunc == tgtfunc and nextblock == tgtblock:
                                        print "Found Callsite Block " + nextfunc + "." + nextblock
					currfunc = tgtfunc
					currblock = tgtblock
	
			if currblock is not None:
				#look for transition out of function from callsite
				if nextblock is None or nextblock != currblock:
					#transition found
                                        print "Found transition " + line 
					transitions.append( ((nextfunc + "." + nextblock) if address is None else address) + " [" + str(lineidx) + "]")
					#print repr(transitions)
					currblock = None
					currfunc = None
					address = None
					
			lineidx += 1
			match = None
	return transitions

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
                dfile.write(currfunction)
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
                    #dfile.write(line)
                    pass
                #if debugactive:
                #    if debugmatcher.match(line) is None:
                #        dfile.write(line);
                #if line == callstr:
                    ofile.write(currfunction+"::"+block+"::" + str(funcidx) + "::" + str(blockidx) + "-->"+line)
                    transitions = findtransitions(currfunction, block , line, tracefilename)
                    print "Transitions are: " +  repr(transitions)
                    for item in transitions:
                            print "\t\t" + item + "\n"
                            ofile.write("\t\t" + item + "\n")
                    continue
                blockidx+=1
                funcidx+=1
            else:
                pass
                #dfile.write(line);
    #if found!= True:
    #    ofile.write("Couldn't find owning func::block for callstr:" + callstr)
  
if __name__ == "__main__":
    processfiles(argv[1], argv[2], argv[3])
