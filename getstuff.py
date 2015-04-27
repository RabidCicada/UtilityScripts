from sys import argv
from subprocess import call
import re

funcmatcher = re.compile(r"^define.*@(.*)\(")
blockmatcher = re.compile(r"^(\S+):")
traceblockmatcher = re.compile(r"^        (\S+)\.(\S+),")
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
	lineidx = 1
	transitions = []
	with open(tracefilename, 'r') as tfile:
		for line in tfile:
			match = traceblockmatcher.match(line)
			if match is not None:
				nextfunc = match.group(1)
				nextblock = match.group(2)
			else:
				nextfunc = None
				nextblock = None

			if nextfunc is not None:
				#start once we found a likely callsite
				if nextfunc == tgtfunc and nextblock == tgtblock:
					currfunc = tgtfunc
					nextblock = tgtblock
	
			if currblock is not None:
				#look for transition out of function from callsite
				if nextblock is None or nextblock != currblock:
					#transition found
					transitions.append(nextfunc + "." + nextblock + " [" + lineidx + "]")
 
			
			lineidx += 1
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
                    transitions = findtransitions(currfunction, block , line, tracefilename)
                    for item in transitions:
			ofile.write("\t" + item)
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
