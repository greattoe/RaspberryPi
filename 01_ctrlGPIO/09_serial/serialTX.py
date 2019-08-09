import serial
import io

ser = serial.serial_for_url('/dev/ttyUSB0', 115200, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

how2 = '''
-------------------------------
If you want to
turn on  red   LED type 'red1',
turn off red   LED type 'red0',
turn on  green LED type 'grn1',
turn off green LED type 'grn0'.
-------------------------------
'''
red0 = "red0\n\r"
red1 = "red1\n\r"
grn0 = "grn0\n\r"
grn1 = "grn1\n\r"

try:
  while(1):
    print how2
    data = input("type command: ")
    print "your input command is", data
    sio.write(unicode(data))
    sio.flush()
    
except KeyboardInterrupt:
  sio.flush()
  ser.close()
  print "\nProgram terminated by user"
