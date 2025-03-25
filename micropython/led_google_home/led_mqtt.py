import network
import machine
import time
from umqtt_simple import MQTTClient

SSID = "iliadbox-20274E"
PASSWORD = "k7bvzq2frkqwddswqnvnws"
MQTT_BROKER = "192.168.1.49"
TOPIC = b"home/pico/led"

mqtt_user ={
  id:"mqtt_user",
  PASSWORD:"Jkd882HnjrqECH"
} 


led = machine.Pin("LED", machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

    
ip = wlan.ifconfig()[0]
print(f"Connected! IP: {ip}")

def mqtt_callback(topic, msg):
    if msg == b"on":
        led.value(1)
    elif msg == b"off":
        led.value(0)

client = MQTTClient(cliend_id="pico", server=MQTT_BROKER,user=mqtt_user[id], password=mqtt_user[PASSWORD])
client.set_callback(mqtt_callback)
client.connect()
client.subscribe(TOPIC)

while True:
    client.wait_msg()
