
import sys
from libyeelight import *
# import machine
# import network
import time

ssid = 'heidi sui monti'
password = 'fioccodineve'

""" def check_connection() -> bool:
  wlan = network.WLAN(network.STA_IF)
  led = machine.Pin("LED", machine.Pin.OUT)
  led.off()
  if wlan.isconnected() is True:
      print("Connesso")
      led.on()
      return True
  else:
      print("Non connesso")
      led.off()
      return False

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
 """

if __name__ == "__main__":
    # connect()
    # if check_connection():
    response = discover_bulb()
    print(response["location"])
    off()
    # on()
      # print(response[""])