# IMPORTS
from machine import Pin
from time import ticks_ms, sleep_ms

# CLASSES
class LedBlink:

    def __init__(self, pin_number, tms):
        self.pin_number = pin_number
        self.tms = tms
        self.led = Pin(self.pin_number, Pin.OUT)
        self.start_time = ticks_ms()
    def blink(self):
       while True:
           if ticks_ms() - self.start_time > self.tms:
                self.led.value(not self.led.value())
                self.start_time = ticks_ms() 
# VARIABLES
led = LedBlink(26, 500)


#print(led.pin_number)
#print(led.tms)
while True: 
    led.blink()
