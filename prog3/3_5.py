################ NEOPIXEL ##############
from neopixel import NeoPixel # Vi skal fra neopixel modulet og hente klassen
from machine import Pin
from time import sleep
import time
import re
import umqtt_robust2 as mqtt


n = 12 # number of pixels in the Neopixel ring
p = 26 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance. Skal have et Pin objekt, derfor Pin(p, Pin.OUT)

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
        np.write()

def clear():
    for i in range(n):
        np[i] = (0,0,0)
        np.write()


############### OPGAVE 3.5 #############################
############### Tænd og sluk forskellige lyseffekter via adafruit, ved at sende tekstbeskeder fx'start bounce' #######
        
while True:
    try:
        if mqtt.besked == "0":
            print('mr 0')
            set_color(126, 1, 0)
            sleep(1)
        elif mqtt.besked == "10":
            print("mr 10")
            set_color(78, 49, 0)
            sleep(1)
        elif mqtt.besked == "20":
            print("mr 20")
            set_color(42, 85, 0)
            sleep(1)
        elif mqtt.besked == "30":
            print("mr 30")
            set_color(18, 109, 0)
            sleep(1)
        elif mqtt.besked == "40":
            print("mr 40")
            set_color(0, 74, 53)
            sleep(1)
        elif mqtt.besked == "50":
            print("mr 50")
            set_color(0, 62, 65)
            sleep(1)
        elif mqtt.besked == "60":
            print("mr 60")
            set_color(9, 0, 118)
            sleep(1)
        elif mqtt.besked == "70":
            print("mr 70")
            set_color(255, 50, 0)
            sleep(1)
        elif mqtt.besked == "80":
            print("mr 80")
            set_color(0, 70, 65)
            sleep(1)
        elif mqtt.besked == "90":
            print("mr 90")
            set_color(0, 2, 125)
            sleep(1)
        elif mqtt.besked == "100":
            print("mr 100")
            set_color(33, 0, 94)
            sleep(1)

        if len(mqtt.besked) != 0:
            mqtt.besked = ""

        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
