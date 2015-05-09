import win32pipe, win32file

serial = open(r'\\.\pipe\serialredirect', 'rb')

while(True):
    data = serial.read()
    
