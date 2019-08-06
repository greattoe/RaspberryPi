import RPi.GPIO as GPIO
from picamera import PiCamera
# from time import sleep

GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN)

camera = PiCamera()

camera.start_preview()
GPIO.wait_for_edge(18, GPIO.RISING)
camera.capture('image.jpg')
camera.stop_preview()