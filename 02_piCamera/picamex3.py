import time
import picamera
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

print "Take picture by SW-input with 5 sec delay"

try:
  # now use "camera" instead "picamera.PiCamera()"
  with picamera.PiCamera() as camera:
    camera.start_preview()
    GPIO.wait_for_edge(18, GPIO.RISING)
  
    for i in range(5):  # for( i=0; i<5; i++ )
      GPIO.output(23, True )
      time.sleep(0.5)
      GPIO.output(23, False)
      time.sleep(0.5)
        
    camera.capture('image.jpg')
    camera.stop_preview()

except KeyboardInterrupt:
	GPIO.cleanup()
	print "\nProgram ended!"