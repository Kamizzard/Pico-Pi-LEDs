from picozero import LED
from time import sleep

led = LED(17)
brightness = 0
i = 3
led.on()

while i > 0:
    led.brightness = brightness    
    for j in range(1,100):
        sleep(0.02)
        brightness += 0.01
        led.brightness = brightness

    for j in range(1,100):
        sleep(0.02)
        brightness -= 0.01
        led.brightness = brightness
    i -= 1
led.off()    
