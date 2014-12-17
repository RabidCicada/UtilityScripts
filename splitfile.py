from sys import argv
from subprocess import call
import re

def processfiles( ifilename, splitmatch, ofilenameprefix ):
    int idx = 0
    with open(ifilename, 'r') as ifile:
        
        ofilename = ifilename+".split." + str(idx) + ".txt"
        ofile =  open(ofilenameprefix, 'w')
        for line in ifile:
            #Get rid of address numbers
            if(line == splitmatch):
                
            #Get rid of offset labels
            line = re.sub(r"<.*>$","",line)
            ofile.write(line)


if __name__ == "__main__":
    processfiles(argv[1], argv[2], argv[3])
