
import sys
from libyeelight import *
import machine
import network
import time

ssid = 'heidi sui monti'
password = 'fioccodineve'
led = None
btn = None
isOn = False
frozeBtn = False

def initBtnAndLed():
  global led, btn
  BUTTON_PIN = 17

  led = machine.Pin("LED", machine.Pin.OUT)
  btn = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)


def check_connection() -> bool:
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

def mainLoop():
   global isOn
   global frozeBtn

   while True:
      btnLoop()

def button_pressed():
    # print("Button pressed!")
    toggleBulb()
    
def toggleBulb():
  global isOn
  
  if isOn:
    isOn = False
    # print("Off")
    off()
  else:
    isOn = True
    # print("On")
    on()
    
def btnLoop():
  if btn.value() == 0:
        button_pressed()
        while btn.value() == 0:
            time.sleep(0.01)  # Debounce delay


if __name__ == "__main__":
    initBtnAndLed()

    connect()
    if check_connection():
      response = discover_bulb()
      print(response["location"])
      resPower = getPower()
      isOn = resPower["result"][0] == "on"
      # print(isOn)
      mainLoop()