from picozero import LED
from time import sleep

i = 25
green = LED(13)
red = LED(16)
blue = LED(17)

while i > 0:
    green.on()
    blue.off()    
    sleep(0.1)
    green.off()
    red.on()
    sleep(0.1)
    blue.on()
    red.off()
    sleep(0.1)
    i -= 1
blue.off()