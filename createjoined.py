from sys import argv
from subprocess import call
from time import sleep
import re

noresetnodebugsuffix = ".noresetnodebug.hex"

def processfiles( ifilename1, ifilename2, offsethexstring, outfilename ):
    print ifilename1, ifilename2
    basefilename1 = ifilename1.replace(".elf","")
    basefilename2 = ifilename2.replace(".elf","")

    print "Executing " + "avr32-objcopy -g -O ihex -R .reset "+ ifilename1 + " " + basefilename1 + noresetnodebugsuffix
    call("avr32-objcopy -g -O ihex -R .reset "+ ifilename1 + " " + basefilename1 + noresetnodebugsuffix)
    print "Executing " + "avr32-objcopy -g -O ihex -R .reset "+ ifilename2 + " " + basefilename2 + noresetnodebugsuffix
    call("avr32-objcopy -g -O ihex -R .reset "+ ifilename2 + " " + basefilename2 + noresetnodebugsuffix)
    print "Executing " + "srec_cat " + basefilename1 + noresetnodebugsuffix + " -intel " + basefilename2 + noresetnodebugsuffix + " -intel -offset " + offsethexstring + " -o " + outfilename + " -intel"
    call("srec_cat " + basefilename1 + noresetnodebugsuffix + " -intel " + basefilename2 + noresetnodebugsuffix + " -intel -offset " + offsethexstring + " -o " + outfilename + " -intel")
    #print "Executing " + "srec_cat at32uc3a3-isp.hex -intel " + outfilename + " -intel -o fullhex.hex -intel"
    #call("srec_cat at32uc3a3-isp.hex -intel " + outfilename + " -intel -o fullhex.hex -intel")

if __name__ == "__main__":
    processfiles(argv[1],argv[2],argv[3],argv[4])
