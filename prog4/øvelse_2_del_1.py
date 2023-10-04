from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel

ANTAL_PIXEL = 12
n = 12
p = 26

np = NeoPixel(Pin(26, Pin.OUT), ANTAL_PIXEL)

def set_color(r, g, b):
    for pixels in range(ANTAL_PIXEL):
        np[pixels] = (r, g, b)
    np.write()
    
def clear():
    for pixel in range(n):
        np[pixel] = (0, 0, 0)
        np.write()
    
pot = ADC(Pin(34, Pin.IN))


while True:
    
    print(pot.read())
    sleep_ms(100)
    
    if pot.read() < 500:
        set_color(255, 0, 0)
    elif pot.read() < 1500:
        set_color(0, 0, 255)
    elif pot.read() > 1500 and pot.read() < 3000:
        set_color(255, 255, 0)
    elif pot.read() > 3000:
        set_color(0, 255, 0)