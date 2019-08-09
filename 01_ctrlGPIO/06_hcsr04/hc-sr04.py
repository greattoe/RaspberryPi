import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 19
ECHO = 26

print "Measurement Distance"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

try:
  while True:
    GPIO.output(TRIG, True)
    time.sleep(0.000010)          # 10 micro sec
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      echo_start = time.time()
      
    while GPIO.input(ECHO)==1:
      echo_end = time.time()
      
    echo_time = echo_end - echo_start
    dist = echo_time * 170000
    dist = round(dist, 2)
    print "Distance = ",dist,"mm"

    time.sleep(1);

except KeyboardInterrupt:
  GPIO.cleanup()