echo Creating joined user application hex file from elf files
python createjoined.py ET024006DHU_EXAMPLE1_modified.elf ET024006DHU_EXAMPLE1_pristine.elf 0x1ba8 joined.hex

echo Programming bootloader hex to micro
atprogram -t avrone -i jtag -d at32uc3a3256 program -c --verify --format hex -f at32uc3a3-isp.hex
echo Programming configuration bits
atprogram -t avrone -i jtag -d at32uc3a3256 program --format bin -o 0x808001f8 -f at32uc3a3-isp-cfg.bin
echo Programming bootloader protection fuses
atprogram -t avrone -i jtag -d at32uc3a3256 write -o 0xFFFE1410 -fs --values FFF5FFFF

echo Please reset the microcontroller into ISP mode by holding SW2 while pressing RESET
pause

batchisp -device at32uc3a3256 -hardware usb -operation erase f memory FLASH blankcheck loadbuffer joined.hex program start reset 0