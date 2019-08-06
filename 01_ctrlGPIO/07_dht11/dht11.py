import RPi.GPIO as GPIO
import DHT11_Python.dht11 as dht11
from time import sleep

GPIO.setmode(GPIO.BCM)

dht = dht11.DHT11(pin=4)

try:
  while True:
    result = dht.read()
    
    if result.is_valid():
      print("T = %-3.1f C" % result.temperature)
      print("H = %-3.1f %%" % result.humidity)
    
    sleep(6)
    
except KeyboardInterrupt:
  GPIO.cleanup()