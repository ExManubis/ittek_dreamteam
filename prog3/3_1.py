import machine, neopixel

# antal pixels
n = 12

# pin den er tilkoblet
p = 15

# neopixel objekt
np = neopixel.NeoPixel(machine.Pin(p), n)

# opgave 3.1
while True:
    for i in range (0,3):
        np[i] = (0, 255, 0)
        np.write()
    for i in range (3,6):
        np[i] = (0, 0, 255)
        np.write()
    for i in range (6,9):
        np[i] = (255, 0, 0)
        np.write()
    for i in range (9,12):
        np[i] = (255, 255, 0) # gul
        np.write()