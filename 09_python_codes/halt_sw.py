#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

pinSW = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSW,GPIO.IN)

def halt(channel):
    os.system("sudo shutdown -h now")
    
print "SW for shutdown is enabled."

try:
    
    GPIO.add_event_detect(pinSW, GPIO.RISING, callback = halt, bouncetime = 400)
    
    while True:
        pass#time.sleep(0.1)
        
except KeyboardInterrupt:
    print "SW for shutdown is disabled."
    GPIO.cleanup()