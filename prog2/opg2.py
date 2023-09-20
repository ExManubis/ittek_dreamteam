import umqtt_robust2 as mqtt
from machine import Pin, PWM,
from time import sleep
# Her kan i placere globale varibaler, og instanser af klasser

buzzer_pin = Pin(26, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)
pwm_buzz.duty(0)    

def buzz(d,t,p):
    pwm_buzz.duty(d) #For at tænde for det, også lydniveau
    pwm_buzz.freq(t) #Toner amn kan få ved at justere på frekvensen i HZ
    sleep(p)
    pwm_buzz.duty(0) #For at slukke den igen

while True:
    try: # Besked/conncention til adafruit. Hvis noget ændres, skal det ske i både Thonny og Adafriut! og små bogstaver!

        if mqtt.besked == "spiller tone a":
            print("spiller tone a!")
            buzz(440, 440, 0.2)
             
        if len(mqtt.besked) != 0:
            mqtt.besked = ""
        
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
