### import block ###
from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel

#Neopixel object
n = 12 # number of pixel in neopixel ring
p = 26 # Pinnumber to controll NeoPixel
neo_p = NeoPixel(Pin(p, Pin.OUT), n) #NeoPixel object neo_p

#potentiometer object
pot = ADC(Pin(34, Pin.IN))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_9BIT)


pot_val = pot.read()


def rotate(r, g, b):
    while True:
        pot_val = pot.read()
        for i in range (n):
            neo_p[i] = (r, g, b)
            neo_p.write()
            sleep_ms(pot_val)
            neo_p[i] = (0, 0, 0)
            print(pot_val)
rotate(40,0,6)