from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT)
pb1 = Pin(4, Pin.IN) # sætter knap til Input

# øvelse 5.1
# while True:
#     print('Knap værdi: ', pb1.value())
#     led1.value(not pb1.value())
#     sleep(0.1)

# øvelse 5.2
# while True:
#     if pb1.value() == 0:
#         led1.value(not led1.value()) # LED skifter hvis knap trykkes

# øvelse 5.3
button_value = 0 # laver en variabel der starter på 0

while True:
    if pb1.value() == 0:
        button_value = button_value + 1
    print(button_value)
    sleep(0.1)


