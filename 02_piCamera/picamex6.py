import sys, os
from picamera import PiCamera
from time import sleep

path = "./Desktop/"
h264 = ".h264"
mp4  = ".mp4"

fName     = sys.argv[1]           # argument for file name to capture
fNameH264 = path + fName + h264
fNameMP4  = path + fName + mp4

secTime = int(sys.argv[2])    # how long wait for to capture image in sec.

camera = PiCamera()

print "start recording..."

camera.start_preview()
camera.start_recording(fNameH264)
sleep(secTime)
camera.stop_recording()
camera.stop_preview()

print "Video Clip ", fNameH264, " is saved!!!"
cmd = "MP4Box -add " + fNameH264 + " " + fNameMP4
os.system(cmd)
print "File converting is finished!"