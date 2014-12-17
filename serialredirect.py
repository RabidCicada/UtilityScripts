import win32pipe, win32file, serial, struct


port = "\\\\.\\COM5"
print "PreComOpen"
serial = serial.Serial(port, 9600)

print "PrePipeOpen"
p = win32pipe.CreateNamedPipe(
    r'\\.\pipe\serialredirect',
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT,
    1, 65536, 65536,
    300,
    None)
win32pipe.ConnectNamedPipe(p, None)

while(True):
    print "preread"
    data = serial.read()
    print "postread"
    tup = struct.unpack('%dB'%len(data),data)
    print "Forwarding data: " + " ".join('0x%02x' % i for i in tup)
    win32file.WriteFile(p, data)
