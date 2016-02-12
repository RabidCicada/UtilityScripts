#!/bin/python
#This script is used along with serialredirect to work around some issues where
#an application cannot read from a com port but can read from a named pipe.

import win32pipe, win32file

serial = open(r'\\.\pipe\serialredirect', 'rb')

while(True):
    data = serial.read()
    
