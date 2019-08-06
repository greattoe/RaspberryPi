#!/usr/bin/python
# line 1 is not comment. that's called 'Shebang' which specifies the interpreter location of 
# scripts.
import RPi.GPIO as GPIO
from os import system

btnPin = 18

GPIO.setmode(GPIO.BCM)       # Use the Broadcom SOC Pin numbers
GPIO.setup(btnPin, GPIO.IN)  # Setup the btnPin as input  
# Setup the btnPin with Internal pullups enabled and PIN in reading mode.
# GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Do next
try:
    print "### Shutdown button is enabled. ###"
    # define function 'shutdown()' which is called back when event is occurred
    def shutdown(channel):
        print("system is going down...")
        system("sudo shutdown -h now")
    
    # detect event(detect falling edge from GPIO 18)
    GPIO.add_event_detect(18, GPIO.FALLING, callback = shutdown, bouncetime = 100)  
    
    # Just wait for switch pressed
    while True:
        pass

# when K/B interrupt occured
except KeyboardInterrupt:
  print "\n### Shutdown button is disabled. ###"
  GPIO.cleanup() 
