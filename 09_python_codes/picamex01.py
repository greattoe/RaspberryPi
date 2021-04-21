import sys # <------
from picamera import PiCamera
from time import sleep

img_name = sys.argv[1] # <------
img_name = "/home/pi/Desktop/" + img_name + ".jpg"
# img_name = "../Desktop/" + img_name + ".jpg"

cam = PiCamera()

#cam.start_preview()
#sleep(5)
cam.capture(img_name)
#cam.stop_preview()