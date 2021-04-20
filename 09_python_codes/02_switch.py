import RPi.GPIO as GPIO

pinLed1 = 21
pinLed2 = 20
pinSW   =  6

GPIO.setmode( GPIO.BCM )
GPIO.setup(pinLed1, GPIO.OUT)
GPIO.setup(pinLed2, GPIO.OUT)
GPIO.setup(pinSW,   GPIO.IN )

print "Press SW or input Ctrl+C to quit"

try:
    while True:
        GPIO.output(pinLed1, True )
        GPIO.output(pinLed2, False)
        
        while GPIO.input(pinSW) == True:
            GPIO.output(pinLed1, False)
            GPIO.output(pinLed2, True )
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print " bye~"