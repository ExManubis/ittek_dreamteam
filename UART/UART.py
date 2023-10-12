# Imports
import sys
import uselect
from machine import UART

# Configuration
uart_remote_port = 1            # Remote UART port
uart_remote_pin_tx = 33         # Remote UART TX pin
uart_remote_pin_rx = 32         # Remote UART RX pin
uart_remote_speed = 9600        # Remote UART speed

# User data
group_id = 8                    # Gruppe nummer

# Objects
uart_remote = UART(uart_remote_port, baudrate = uart_remote_speed, tx = uart_remote_pin_tx, rx = uart_remote_pin_rx)

usb = uselect.poll()
usb.register(sys.stdin, uselect.POLLIN)

# Functions

# Program
print('Two-way ESP32 remote data system\n')

while True:
    # 
    if uart_remote.any() > 0:
        string = uart_remote.read().decode()
        string = string.strip()
        print('Remote: ' + string)

    if usb.poll(0):
        string = sys.stdin.readline()
        sys.stdin.readline()
        string = string.strip()
        print('USB  : ' + string)

        uart_remote.write(string + '\n')