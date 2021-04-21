#!/usr/bin/python
# !/usr/bin/python

# import RPi.GPIO as GPIO
from RPi  import GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

print "GPIO Test~, press Ctrl+C to quit"

try:
    while True:
        GPIO.output(21, False)
        GPIO.output(20, True )
        sleep(0.5)
        
        GPIO.output(21, True )
        GPIO.output(20, False)
        sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print " bye~"
