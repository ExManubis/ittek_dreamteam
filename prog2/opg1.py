import umqtt_robust2 as mqtt
from machine import Pin

led3 = Pin(13, Pin.OUT)

while True:
    try:
        if mqtt.besked == "led3 on":
            led3.on()
        elif mqtt.besked == "led3 off":
            led3.off()