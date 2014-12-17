from sys import argv
from subprocess import call
import shutil
import hashlib
import win32api, win32gui, win32con, win32file, struct
import string
from ctypes import windll
import time
import os

DDDrive = ""
testFile = "testextfile.txt"
testFileHash = None
expectedFile = "expectedtext.txt"
expectedFileHash = None

FSCTL_LOCK_VOLUME = 0x0090018
FSCTL_DISMOUNT_VOLUME = 0x00090020
IOCTL_STORAGE_MEDIA_REMOVAL = 0x002D4804
IOCTL_STORAGE_EJECT_MEDIA = 0x002D4808


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def remountVolume(driveName):
        dwDesiredAccess = win32con.GENERIC_READ|win32con.GENERIC_WRITE
        dwShareMode = win32con.FILE_SHARE_READ|win32con.FILE_SHARE_WRITE
        dwCreationDisposition = win32con.OPEN_EXISTING

        hVolume = win32file.CreateFile(lpFileName, dwDesiredAccess, dwShareMode, None, dwCreationDisposition, 0, None)
        try:
            win32file.DeviceIoControl(hVolume, FSCTL_LOCK_VOLUME, "", 0, None)
            win32file.DeviceIoControl(hVolume, FSCTL_DISMOUNT_VOLUME, "", 0, None)
            win32file.DeviceIoControl(hVolume, FSCTL_UNLOCK_VOLUME, "", 0, None)
        #
        #        win32file.DeviceIoControl(hVolume, IOCTL_STORAGE_MEDIA_REMOVAL, struct.pack("B", 0), 0, None)
        #        win32file.DeviceIoControl(hVolume, IOCTL_STORAGE_EJECT_MEDIA, "", 0, None)
        #except:
        #        raise
        finally:
            win32file.CloseHandle(hVolume)
        #time.sleep(3)

        #force re-enumaration ( According to FSCTL_DISMOUNT_VOLUME control code developer page on MSDN this forces a re-enumeration )
        windll.kernel32.GetLogicalDrives()

        #from win32com.shell import shell, shellcon 
        #shell.SHChangeNotify(shellcon.SHCNE_DRIVEREMOVED, shellcon.SHCNF_PATH, "F:\\")

def formatAndTest(driveletter):
    print "Formatting Drive"
    call("diskpart /S darkdriveformatscript.txt")

    print "Copying Test file to Drive"
    shutil.copyfile(testFile,DDDrive+testFile)   

    print "Forcing remount of volume to flush cache..."
    remountVolume(driveletter)

    print "Comparing read-back test file to expected results"
    with open(expectedFile, 'rb') as efile:
        expectedFileHash = hashlib.sha1(expectedFile.read()).hexdigest()

    with open(DDDrive+testFile, 'rb') as tfile:
        testFileHash = hashlib.sha1(expectedFile.read()).hexdigest()

    if testFileHash == expectedFileHash:
        print "Drive Appears VALID!"
        
if __name__ == "__main__":

    before = set(get_drives())

    #periodically poll for new drives
    #perform format and test for each drive
    while True:
        after = set(get_drives())
        drives = after - before
        delta = len(drives)

        if (delta):
            for drive in drives:
                if os.system("cd " + drive + ":") == 0:
                    newly_mounted = drive
                    print "There were %d drives added: %s. Newly mounted drive letter is %s" % (delta, drives, newly_mounted)
                    formatAndTest(newly_mounted)

        
        time.sleep(1)
                    
    
    
    
    
