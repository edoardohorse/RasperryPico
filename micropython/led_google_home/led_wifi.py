import network
import socket
import machine

ssid = "iliadbox-20274E"
password = "k7bvzq2frkqwddswqnvnws"

led = machine.Pin("LED", machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

ip = wlan.ifconfig()[0]
print(f"Connected! IP: {ip}")

def web_page():
    return """<html>
    <head><title>Pico W LED Control</title></head>
    <body>
    <h2>LED Control</h2>
    <a href="/on"><button>Turn On</button></a>
    <a href="/off"><button>Turn Off</button></a>
    </body></html>"""

def handle_request(request):
    request = str(request)
    if "/on" in request:
        led.value(1)
    elif "/off" in request:
        led.value(0)

server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(5)

while True:
    conn, addr = server.accept()
    request = conn.recv(1024)
    handle_request(request)
    response = web_page()
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + response)
    conn.close()
