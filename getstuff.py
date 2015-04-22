from sys import argv
from subprocess import call
import re


def processfiles( callsfname, llvmfname, ofilename ):
    currfunction = None
    block = None
    with open(callsfname, 'r'),open(llvmfname, 'r'),open(ofilename, 'w') as callsfile,llvmfile,ofile:
    for callstr in callsfile:
	for line in llvmfile:
	
        #Get rid of address numbers
        match  = re.match(r"^define.*@(.*)\(",line)
	if match is not None:
		currfunction = match.group(1)
		continue #get next line

	if currfunction is not None:
        	#Get rid of offset labels
        	match = re.match(r"^(\S+):",line)
		if match is not None:
			block = match.group(1)
	
	if block is not None:
		if line == callstr
			break #found our string and have all info

	
	ofile.write(currfunction+"::"+block+"-->"+callstr)

if __name__ == "__main__":
    processfiles(argv[1], argv[2], argv[3])
