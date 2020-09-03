## Programming the Atmega328p from Raspberry Pi

Install arduino and avrdude with 

    sudo apt update
    sudo apt install arduino arduino-mk avrdude -y
    
Make sure to enable SPI from interfacing options in raspi-config

#### Wiring

DO NOT CONNECT ATMEGA TO 5V DURING PROGRAM UPLOAD, rpi GPIO pins can only handle 3.3v. Connext Atmega VCC, AVCC, AREF to RPi 3v3, and ground to RPi ground. Atmega reset pin should be pulled up by a 10k resistor and connected to GPIO 25. Connect MISO, MOSI and SCK on Atmega to MISO, MOSI, and SCLK on Rpi. 

Note: Because we are programming at 3.3V we have to lower the baud rate to 200000.

Check connections from RPi by running 

    sudo avrdude -c linuxspi -p m328p -P /dev/spidev0.0 -b 200000

You should get a valid device signature. If not check connections.

#### Compile and upload

Run `make` from one of the directories such as `blink-test` to compile the code for the Atmega. Then, run

    sudo avrdude -p m328p -c linuxspi -P /dev/spidev0.0 -e -U flash:w:build-uno/dir-name.hex -b 200000

Replacing `dir-name` with the name of the directory you're uploading.  

