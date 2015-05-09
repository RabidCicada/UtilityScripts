from sys import argv
from subprocess import call
from time import sleep
import re

headersinfosuffix = ".info.txt"
dissasmsuffix = ".diss.txt"
strippedsuffix = ".stripped"
strippedheaderinfosuffix = ".stripped.info.txt"
sizesuffix = ".size.txt"
noresetbinarysuffix = ".noreset.bin"

def processfiles( ifilename ):
    print ifilename
    
    call("avr32-objdump -x "+ ifilename, stdout=open(ifilename+headersinfosuffix,"wb"))
    call("avr32-objcopy -g "+ ifilename + " " + ifilename + strippedsuffix)
    call("avr32-objdump -x "+ ifilename + strippedsuffix, stdout=open(ifilename+strippedheaderinfosuffix,"wb"))
    call("avr32-objdump -D -m avr32 " + ifilename + strippedsuffix,stdout=open(ifilename+dissasmsuffix,"wb"))
    call("avr32-size -A -x " + ifilename + strippedsuffix,stdout=open(ifilename+sizesuffix,"wb"))

if __name__ == "__main__":
    processfiles(argv[1])
