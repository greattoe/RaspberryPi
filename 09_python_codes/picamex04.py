import sys
import time
import picamera
import RPi.GPIO as GPIO 

fName = sys.argv[1]						        # test02
fName = "/home/pi/Desktop/" + fName +".jpg"	# fName = "./Desktop/test02.jpg
secTime = int(sys.argv[2])  			    # sys.argv[2]="3" --> 3

GPIO.setmode(GPIO.BCM) 
GPIO.setup(6, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

print "Take picture by SW-input with ", secTime, "sec delay~"

try:
  # now use "camera" instead "picamera.PiCamera()"
  with picamera.PiCamera() as camera:
    camera.start_preview()
	
    GPIO.wait_for_edge(6, GPIO.RISING) 
    # while GPIO.input(18) == 0:
    #   pass
  
    for i in range(secTime):  # for( i=0; i<5; i++ )
      GPIO.output(21, True )
      time.sleep(0.5)
      GPIO.output(21, False)
      time.sleep(0.5)
        
    camera.capture(fName)
    camera.stop_preview()

except KeyboardInterrupt:
	GPIO.cleanup()
	print "\nbye~"