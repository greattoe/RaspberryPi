import sys
from picamera import PiCamera
from time import sleep

fName = sys.argv[1]           # argument for file name to capture
fName = "./Desktop/" + fName
secTime = int(sys.argv[2])    # how long wait for to capture image in sec.

camera = PiCamera()

camera.start_preview()
camera.capture(fName)
sleep(secTime)
camera.stop_preview()

print "picture ./Desktop/",sys.argv[1]," is saved!!!"
