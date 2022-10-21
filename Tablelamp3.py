#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause
from time import sleep

print ('Program is starting ... ')

led = LED(17) # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

strobe = 0

def onButtonPressed():
    global strobe
    strobe += 1
    if strobe == 6:
        strobe = 0
    print(strobe)

button.when_pressed = onButtonPressed

while True:
    if strobe == 0:
        led.off()
    if strobe == 1:
        led.on()
    if strobe == 2:
        while strobe == 2:
            led.toggle()
            sleep(1)
    if strobe == 3:
        while strobe == 3:
            led.toggle()
            sleep(.5)
    if strobe == 4:
        while strobe == 4:
            led.toggle()
            sleep(.05)
    if strobe == 5:
        led.off()
        strobeLength = 0
        while strobe == 5:
            led.on()
            if strobeLength == 0:
                sleep(1)
                strobeLength = 1
            else:
                sleep(.25)
                strobeLength = 0
            led.off()
            sleep(1)
