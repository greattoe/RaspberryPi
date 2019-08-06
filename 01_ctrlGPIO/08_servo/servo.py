import RPi.GPIO as GPIO
from time import sleep
import sys, tty, termios

servo = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch

pulse = GPIO.PWM(servo, 50) # GPIO 17 for PWM with 50Hz
pulse.start(2.5) # Initialization

print "Servo Control Test~"
print "Control Input: "
ch = getch()
print ch

pos    =  7.5
offset =  0.5

MIN    =  2.5
MAX    = 12.5

try:
  while ch != 'Q':
    
    print "Control Input: "
    ch = getch()
    print ch
    
    if ch == '.': # '>'
      if pos <= MAX - offset:
        pos = pos + offset
      else:
        pos = MAX
    
    elif ch == ',': # '<'
      if pos >= MIN + offset:
        pos = pos - offset
      else:
        pos = MIN
        
    elif ch == '1':
      pos =  2.5
      
    elif ch == '2':
      pos =  5.0
        
    elif ch == '3':
      pos =  7.5
      
    elif ch == '4':
      pos = 10.0
        
    elif ch == '5':
      pos = 12.5
      
    else:
      pass
      
    pulse.ChangeDutyCycle(pos)
    sleep(0.5)
    
    print "servo positon = ", pos
    
except KeyboardInterrupt:
  pulse.stop()
  GPIO.cleanup()