# importerer nødvendige classes + functions
from machine import Pin 
from time import sleep

# definerer de 3 LED'er og deres funktion 
RED_PIN = 26 # sætter variablen RED_PIN til 12
led1 = Pin(RED_PIN, Pin.OUT) # Pin.OUT da vi skal bruge dem som output

YELLOW_PIN = 12
led2 = Pin(YELLOW_PIN, Pin.OUT) 

GREEN_PIN = 13
led3 = Pin(GREEN_PIN, Pin.OUT)

# øvelse 4.1
# while  True: # while loop
#         led1.value(not led1.value()) # sætter led1 til det omvendte af hvad den er lige nu
#         sleep(1) # pauser programmet i 1 sekund

# øvelse 4.2
# while True:
#     led1.value(not led1.value())
#     sleep(0.5) # pauser i 0.5 sek.

# øvelse 4.3
# while True:
#     led3.value(not led3.value()) # grøn LED = led3
#     sleep(0.01) # 0.01 sekund kan man (næsten) ikke se at den slukker

# øvelse 4.4
# sørger for at alle LED er slukket
led1.off()
led2.on() # led2 sættes til on, da det slukker den, da den er aktiv lav
led3.off()
# laver en toggle_all funktion
def toggle_all():
    led1.value(not led1.value())
    led2.value(not led2.value())
    led3.value(not led3.value())
#                
# while True:
#     toggle_all() # skifter LED mellem tænd/sluk
#     sleep(1) # venter 1 sekund#

# øvelse 4.5
# laver en toggle funktion med name som argument, så man ikke skal skrive så meget kode
# def toggle(name):
#     name.value(not name.value())
#     sleep(1)
#     name.value(not name.value())
#     sleep(1)
#     
# while True:
#     toggle(led1) # bruger toggle funktionen til led1, 2 etc
#     toggle(led2)
#     toggle(led3)

# øvelse 4.6 (lyskryds)
# laver simpel toggle funktion
def toggle(name):
    name.value(not name.value())
    
while True:
    toggle(led1)
    sleep(15)
    toggle(led2)
    sleep(5)
    toggle(led1); toggle(led2); toggle(led3) # skifter alle LED på samme tid
    sleep(10)
    toggle(led3)

