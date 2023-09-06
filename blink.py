from  machine import Pin
from time import sleep

RedPin = 26

led1 = Pin(RedPin, Pin.OUT)

# 1 sekond interval
while True:
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)