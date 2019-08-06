import sys
from picamera import PiCamera
from time import sleep

fName = sys.argv[1]           # name of video file to record
secTime = int(sys.argv[2])    # argument for how long time to record video

camera = PiCamera()

camera.start_preview()
camera.start_recording(fName)
sleep(secTime)
camera.stop_recording()
camera.stop_preview()

print sys.argv[2],"sec clip is saved as name ",sys.argv[1]