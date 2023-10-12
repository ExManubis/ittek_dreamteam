# Imports
import sys
import uselect
from machine import UART, Pin, ADC

# Configuration
uart_remote_port = 1            # Remote UART port
uart_remote_pin_tx = 33         # Remote UART TX pin
uart_remote_pin_rx = 32         # Remote UART RX pin
uart_remote_speed = 9600        # Remote UART speed

battery = ADC(Pin(25, Pin.IN)) 

# User data
group_id = '8'                    # Gruppe nummer
batVoltage = battery.read()

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
        if string == 'rd group':
            string = group_id
            uart_remote.write(string + '\n')
        elif string == 'rd bat':
            string = str(batVoltage)
            uart_remote.write(string + '\n')
        else:    
            print('Remote: ' + string)

    if usb.poll(0):
        string = sys.stdin.readline()
        sys.stdin.readline()
        string = string.strip()
        print('USB  : ' + string)

        uart_remote.write(string + '\n')