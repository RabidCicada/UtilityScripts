#!/bin/python
#This script will programmatically eject a removable storage drive for windows
#It first dismounts teh filesystem then ejects the media

import win32api, win32gui, win32con, win32file, struct

FSCTL_LOCK_VOLUME = 0x0090018
FSCTL_DISMOUNT_VOLUME = 0x00090020
IOCTL_STORAGE_MEDIA_REMOVAL = 0x002D4804
IOCTL_STORAGE_EJECT_MEDIA = 0x002D4808


lpFileName = r"\\.\F:"
dwDesiredAccess = win32con.GENERIC_READ|win32con.GENERIC_WRITE
dwShareMode = win32con.FILE_SHARE_READ|win32con.FILE_SHARE_WRITE
dwCreationDisposition = win32con.OPEN_EXISTING

hVolume = win32file.CreateFile(lpFileName, dwDesiredAccess, dwShareMode, None, dwCreationDisposition, 0, None)
win32file.DeviceIoControl(hVolume, FSCTL_LOCK_VOLUME, "", 0, None)
win32file.DeviceIoControl(hVolume, FSCTL_DISMOUNT_VOLUME, "", 0, None)
try:
	win32file.DeviceIoControl(hVolume, IOCTL_STORAGE_MEDIA_REMOVAL, struct.pack("B", 0), 0, None)
	win32file.DeviceIoControl(hVolume, IOCTL_STORAGE_EJECT_MEDIA, "", 0, None)
except:
	raise
finally:
	win32file.CloseHandle(hVolume)

from win32com.shell import shell, shellcon 
shell.SHChangeNotify(shellcon.SHCNE_DRIVEREMOVED, shellcon.SHCNF_PATH, 
"F:\\") 
