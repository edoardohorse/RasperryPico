import network
import machine
import time
from logger import log
from umqtt_simple import MQTTClient

SSID = "iliadbox-20274E"
PASSWORD = "k7bvzq2frkqwddswqnvnws"
MQTT_BROKER = "192.168.1.49"
TOPICS={
  "set_state":"pico/led",
  "get_state":"pico/led/state"
}

VALUE_ON = 1
VALUE_OFF = 0

MQTT_USER ={
  id:"mqtt_user",
  PASSWORD:"Jkd882HnjrqECH"
} 
CLIENT_ID="pico"


led = machine.Pin("LED", machine.Pin.OUT)
client: MQTTClient
wlan: network.WLAN

def connectWifi():
  global wlan
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(SSID, PASSWORD)

  while not wlan.isconnected():
      time.sleep(1)
   


def printInfo():
  global wlan
  ip = wlan.ifconfig()[0]
  log(f"Connected Wifi! Your IP is: {ip}")
  print(f"USER: {MQTT_USER[id]}\nBROKER_SERVER: {MQTT_BROKER}\nTOPIC: {TOPICS}")

  # MQTT Callback
def on_message(topic, msg):
  message = msg.decode()
  log(f"Received message of topic: {topic.decode()} -> {message}")


  if topic.decode() == TOPICS["set_state"]:
    if message == str(VALUE_ON):
      log("Led on")
      led.value(VALUE_ON)
    elif message == str(VALUE_OFF):
      log("Led off")
      led.value(VALUE_OFF)
        

def init():
  global led, client

  led.value(0)
  client = MQTTClient(client_id=CLIENT_ID, server=MQTT_BROKER,user=MQTT_USER[id], password=MQTT_USER[PASSWORD])
  client.set_callback(on_message)
  client.connect()
  client.subscribe(TOPICS["set_state"])
  print("Listening for MQTT messages...")

def main():
  connectWifi()
  printInfo()
  init()
  while True:
    client.wait_msg()

      
    # You can also send periodic state updates
    # Example: sending an "ON" or "OFF" state periodically
    time.sleep(2)
    value_led = str(VALUE_ON if led.value() else VALUE_OFF)
    client.publish(TOPICS["get_state"], value_led, retain=True)

main()