echo Programming bootloader hex to micro
atprogram -t avrone -i jtag -d at32uc3a3256 program -c --verify --format hex -f fullhex.hex
echo Programming configuration bits
atprogram -t avrone -i jtag -d at32uc3a3256 program --format bin -o 0x808001f8 -f at32uc3a3-isp-cfg-alwaysbootload.bin
echo Programming bootloader protection fuses
atprogram -t avrone -i jtag -d at32uc3a3256 write -o 0xFFFE1410 -fs --values FFF5FFFF