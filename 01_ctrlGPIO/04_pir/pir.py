import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.IN )

GPIO.output(23, False)
GPIO.output(24, False)

print "PIR Sensor Test"

try:
  while True:
    if GPIO.input(18) == 0:
      GPIO.output(23, False)
      GPIO.output(24, True )
    else:
      GPIO.output(23, False)
      GPIO.output(24, True )

except KeyboardInterrupt:
  GPIO.cleanup()
  print "\n", "Program Terminatepd!"
