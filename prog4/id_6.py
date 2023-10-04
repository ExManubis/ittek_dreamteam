import umqtt_robust2 as mqtt
from machine import Pin, PWM
from time import sleep
import time
from random import choice

klaver = [220, 246, 130, 146, 164, 174]
buzzer_pin = Pin(15, Pin.OUT)
PWM_buzzer = PWM(buzzer_pin, duty=0)

def play(key,time):
    PWM_buzzer.duty(200)
    PWM_buzzer.freq(key)
    sleep(time)
    PWM_buzzer.duty(0)
    sleep(time)


while True:
    try:
        
        if mqtt.besked == "spil random toner":
            print("Spiller første tone!")
            play(choice(klaver), 1)
            print("Spiller anden tone!")
            play(choice(klaver), 1)  
            print("Spiller tredje tone!")
            play(choice(klaver), 1)