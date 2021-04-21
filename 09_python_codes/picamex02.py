import sys
import RPi.GPIO as GPIO
from picamera import PiCamera

img_name = sys.argv[1]
img_name = "/home/pi/Desktop/" + img_name + ".jpg"

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

camera = PiCamera()

try:
    camera.start_preview()
    GPIO.wait_for_edge(6, GPIO.RISING)
    camera.capture(img_name)
    camera.stop_preview()

except KeyboardInterrupt:
    GPIO.cleanup()