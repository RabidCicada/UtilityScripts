import serial, struct, time

CMD_READ_PM = 0x02
CMD_READ_ID = 0x09
CMD_NACK_RESET_DEV = 0x00
port = "\\\\.\\COM4"
rowsize = 64*8  #Based on chip familly 33f in our case

def readPM(serPort, addr):
    addr = addr-(addr%(rowsize*2))
    cmd = chr(CMD_READ_PM) + chr(addr & 0xff) + chr((addr >>8) & 0xff) + chr((addr >>16) & 0xff)
    serPort.write(cmd)

    data = serial.read(rowsize*3)
    tup = struct.unpack('%dB'%len(data),data)
    print "Got data: " + " ".join('0x%02x' % i for i in tup)
    
if __name__ == "__main__":
    print "PreComOpen"
    serial = serial.Serial(port, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 1)
    print serial.portstr
    print "Trying to get device version"
    serial.write(chr(CMD_READ_ID))
    data = serial.read(8)
    tup = struct.unpack('%dB'%len(data),data)
    print "Got data: " + " ".join('0x%02x' % i for i in tup)
    readPM(serial,0x000400)
    print "Resetting device"
    serial.write(chr(CMD_NACK_RESET_DEV))



    
    
