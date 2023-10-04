from machine import Pin, ADC
from time import sleep_ms

pot = ADC(Pin(34, Pin.IN), atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT) # 9BIT maks lidt over 500, 10BIT maks lidt over 1000, 11BIT maks lidt over 2000, 12BIT maks lidt over 4000  
led1 = Pin(26, Pin.OUT, value=0)

while True:
    pot_val = pot.read()
    spaending = pot_val * (3.3/4096)
    print("Analog potentiometer vaerdi:   ", pot_val)
    print("\nAnalog potentiometer spaending: ", spaending)
    led1.value(not led1.value())
    sleep_ms(pot_val)