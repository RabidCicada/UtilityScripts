#!/bin/python

#This script is used to parse through a pdf document as exported to text by
#adobe pdf It looks through the text file for the key phrase and names the
#original pdf document according to the key phrase.

from sys import argv
import os
from subprocess import call
from time import sleep
import win32com.client
import glob
import re

def getPdfFirstLine(fname):
    f = file(fname,"rb")
    pdf = pyPdf.PdfFileReader(f)
    print pdf.getPage(0).extractText()

def processfiles( dir ):
    global shell
    for filepath in glob.glob(dir+'*.pdf'):
        dir = os.path.abspath(dir) + "\\"
        filename = os.path.basename(filepath)
        print dir+filename
        basefilename =filename.replace(".pdf","")

        #save the file to text
        #adobe breaks a lot of stuff when it does so.
        os.startfile(dir+filename)
        sleep(2)
        shell.AppActivate(filename)
        shell.SendKeys('%fax')
        sleep(2)
        shell.SendKeys(dir+basefilename+".txt")
        shell.SendKeys('{ENTER}')
        sleep(25)
        shell.SendKeys('%fx')
        sleep(2)

        #grep through the document looking for the section name
        print dir+basefilename+".txt"
        with open(dir+basefilename+".txt", 'r') as ifile:
            for line in ifile:
                match = re.match(r'(Section \d{1,3})\.(.*)',line)
                
                if match:
                    #print match.group(0)
                    #print match.group(1)
                    #print match.group(2)
                    sectionnum = re.sub(r'\s',r'',match.group(1))
                    title = re.sub(r'\s|[\/{()<>}"']',r'',match.group(2))
                    print dir+filename,dir+sectionnum+"-"+title+"-"+basefilename+".pdf"
                    os.rename(dir+filename,dir+sectionnum+"-"+title+"-"+basefilename+".pdf")
                    break
        
if __name__ == "__main__":
    shell = win32com.client.Dispatch("WScript.Shell")
    processfiles(argv[1])
