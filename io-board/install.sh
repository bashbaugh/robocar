
# Install arduino and avrdude for programming the ATmega through SPI from the raspberry pi
# SPI must be enabled through raspi-config

sudo apt update

sudo apt install arduino arduino-mk avrdude -y

sudo avrdude -p atmega328p -c linuxspi -P /dev/spidev0.0
