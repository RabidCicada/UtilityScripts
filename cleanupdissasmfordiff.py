from sys import argv
from subprocess import call
import re

def processfiles( ifilename, ofilename ):
    with open(ifilename, 'r') as ifile,open(ofilename, 'w') as ofile:
        for line in ifile:
            #Get rid of address numbers
            line = re.sub(r"^[0-9a-z]{8}:?\s","",line)
            #Get rid of offset labels
            line = re.sub(r"<.*>$","",line)
            ofile.write(line)


if __name__ == "__main__":
    processfiles(argv[1], argv[2])
