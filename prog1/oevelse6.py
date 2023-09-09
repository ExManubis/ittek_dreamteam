from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT)
pb1 = Pin(4, Pin.IN) # sætter knap til Input

# øvelse 6.1 + 6.2
while True:
    first = pb1.value()
    sleep(0.1)
    second = pb1.value()
    if first == 1 and second == 0:
        led1.value(not led1.value())