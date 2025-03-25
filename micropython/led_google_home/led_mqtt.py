import network
import machine
import time
from umqtt_simple import MQTTClient

SSID = "iliadbox-20274E"
PASSWORD = "k7bvzq2frkqwddswqnvnws"
MQTT_BROKER = "192.168.1.49"
TOPIC = "home/pico/led"

MQTT_USER ={
  id:"mqtt_user",
  PASSWORD:"Jkd882HnjrqECH"
} 
CLIENT_ID="pico"


led = machine.Pin("LED", machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

    
ip = wlan.ifconfig()[0]

def printInfo():
  print(f"Connected Wifi IP! Your IP is: {ip}")
  print(f"USER: {MQTT_USER[id]}\nBROKER_SERVER: {MQTT_BROKER}\nTOPIC: {TOPIC}")

def mqtt_callback(topic, msg):
    if msg == b"on":
        led.value(1)
    elif msg == b"off":
        led.value(0)

printInfo()
client = MQTTClient(client_id=CLIENT_ID, server=MQTT_BROKER,user=MQTT_USER[id], password=MQTT_USER[PASSWORD])
client.set_callback(mqtt_callback)
client.connect()
client.subscribe(TOPIC)

while True:
    client.wait_msg()
