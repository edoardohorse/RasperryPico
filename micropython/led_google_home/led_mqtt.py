import network
import machine
import time
from logger import log
from umqtt_simple import MQTTClient

SSID = "iliadbox-20274E"
PASSWORD = "k7bvzq2frkqwddswqnvnws"
MQTT_BROKER = "192.168.1.49"
TOPIC = "pico/led"

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
  print(f"USER: {MQTT_USER[id]}\nBROKER_SERVER: {MQTT_BROKER}\nTOPIC: {TOPIC}")

  # MQTT Callback
def on_message(topic, msg):
  message = msg.decode()
  log(f"Received message of topic: {topic.decode()}")
  
  if msg == b"on":
      log("Led on")
      led.value(1)
  elif msg == b"off":
      log("Led off")
      led.value(0)

def init():
  global led, client

  led.value(0)
  client = MQTTClient(client_id=CLIENT_ID, server=MQTT_BROKER,user=MQTT_USER[id], password=MQTT_USER[PASSWORD])
  client.set_callback(on_message)
  client.connect()
  client.subscribe(TOPIC)
  print("Listening for MQTT messages...")

def main():
  connectWifi()
  printInfo()
  init()
  while True:
      client.wait_msg()

main()