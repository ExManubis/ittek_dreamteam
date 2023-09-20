import umqtt_robust2 as mqtt
from machine import Pin, PWM,
from time import sleep
from gpio_lcd import GpioLcd

# Her kan i placere globale varibaler, og instanser af klasser
buzzer_pin = Pin(26, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)
pwm_buzz.duty(0)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22), num_lines=4, num_columns=20)
lcd.clear()
lcd.putstr("Hej Valdemar, jeg er fanget herinde, hjælp!")

sleep_time_short = 0.1

def buzz(d,t,p):
    pwm_buzz.duty(d) #For at tænde for det, også lydniveau
    pwm_buzz.freq(t) #Toner amn kan få ved at justere på frekvensen i HZ
    sleep(p)
    pwm_buzz.duty(0) #For at slukke den igen
    

while True:
    try: # Besked/conncention til adafruit. Hvis noget ændres, skal det ske i både Thonny og Adafriut! og små bogstaver!
            
        if mqtt.besked == "you want imperial?":
             lcd.putstr("may the force be with you")
             buzz(50, 329, 0.2),
             sleep(0.5)
             buzz(50, 329, 0.2),
             sleep(0.5)
             buzz(50, 329, 0.2),
             sleep(0.5)
             buzz(50, 261, 0.2),
             sleep(0.2)
             buzz(50, 392, 0.2),
             sleep(0.2)
             buzz(50, 329, 0.2),
             sleep(0.5)
             buzz(50, 261, 0.2),
             sleep(0.2)
             buzz(50, 392, 0.2),
             sleep(0.2)
             buzz(50, 329, 0.2),
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
