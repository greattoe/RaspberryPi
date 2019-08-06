import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BCM )

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.IN )

print "Press SW or input Ctrl+C to quit"

try:
  while True:
    GPIO.output(23, False)
    GPIO.output(24, False)

    while GPIO.input(18) == 0:
      GPIO.output(23, True)
      GPIO.output(24, True)

except KeyboardInterrupt:
  GPIO.cleanup()
  print "\nbye~"
