from picozero import pico_led
from time import sleep

i = 15

while i > 0:
    pico_led.on()
    sleep(0.1)
    pico_led.off()
    sleep(0.1)
    i -= 1
    print(i)