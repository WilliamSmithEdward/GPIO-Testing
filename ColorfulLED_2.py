#!/usr/bin/env python3
########################################################################
# Filename    : ColorfulLED_2.py
# Description : Spectrum Cycle ColorfulLED
# Author      : William Smith
# modification: 2022/10/25
########################################################################
import RPi.GPIO as GPIO
import time
import random

pins = [11, 12, 13]         # define the pins for R:11,G:12,B:13 

def setup():
    global pwmRed,pwmGreen,pwmBlue  
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(pins, GPIO.OUT)     # set RGBLED pins to OUTPUT mode
    GPIO.output(pins, GPIO.HIGH)   # make RGBLED pins output HIGH level
    pwmRed = GPIO.PWM(pins[0], 2000)      # set PWM Frequence to 2kHz
    pwmGreen = GPIO.PWM(pins[1], 2000)  # set PWM Frequence to 2kHz
    pwmBlue = GPIO.PWM(pins[2], 2000)    # set PWM Frequence to 2kHz
    pwmRed.start(0)      # set initial Duty Cycle to 0
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(r_val,g_val,b_val):      # change duty cycle for three pins to r_val,g_val,b_val
    pwmRed.ChangeDutyCycle(r_val)     # change pwmRed duty cycle to r_val
    pwmGreen.ChangeDutyCycle(g_val)   
    pwmBlue.ChangeDutyCycle(b_val)

def loop():
    r=0
    g=100
    b=100
    
    mode='r'
    
    while True :
        
        if mode == 'r':
            r += 1
            b -= 1
            if r == 100:
                mode = 'b'
        
        if mode == 'b':
            b += 1
            g -= 1
            if b == 100:
                mode = 'g'
        
        if mode == 'g':
            g += 1
            r -= 1
            if g == 100:
                mode = 'r'
                    
        setColor(r,g,b)          #set as a duty cycle value 
        
        print ('r=%d, g=%d, b=%d ' %(r ,g, b))
        time.sleep(.1)
        
def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
