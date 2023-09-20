#Import block
import umqtt_robust2 as mqtt
from time import sleep
from machine import Pin

buttonpin = 4
mybutton = Pin(buttonpin,Pin.IN)

while True:
    try:
                        #sætter web_print til 1. som skifter indikator når Ada fanger den.
        if mybutton.value() == 0:
            mqtt.web_print("1")
            sleep(5)
            
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
        mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
        except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
            print('Ctrl-C pressed...exiting')
            mqtt.c.disconnect()
            mqtt.sys.exit()