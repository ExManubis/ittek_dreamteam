from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12 
p = 26 
np = NeoPixel(Pin(p, Pin.OUT), n) 

def set_color(r, g, b):
    for pixel in range(n):
        np[pixel] = (r, g, b)
        np.write()
        sleep(0.3)
    
    
def clear():
    for pixel in range(n):
        np[pixel] = (0, 0, 0)
        np.write()
        
set_color(0, 0, 255)
clear()