#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

pinLed1 = 21
pinLed2 = 20
pinSW   =  6

GPIO.setmode( GPIO.BCM )
GPIO.setup(pinLed1, GPIO.OUT)
GPIO.setup(pinLed2, GPIO.OUT)
GPIO.setup(pinSW,   GPIO.IN )

count = 0

#def check_sw():
    

print "Press SW or input Ctrl+C to quit"

try:
    while True:
    
        if GPIO.input(pinSW) == True:
            sleep(0.160)
            
            if GPIO.input(pinSW) == True:
            
                if count == 10000:
                    count = 0
                count = count + 1
        
        if count % 2 == 1:
            GPIO.output(pinLed1, True )
            GPIO.output(pinLed2, False)
        else:
            GPIO.output(pinLed1, False)
            GPIO.output(pinLed2, True )
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print " bye~"