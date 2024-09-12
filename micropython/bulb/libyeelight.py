""" https://www.yeelight.com/download/Yeelight_Inter-Operation_Spec.pdf """

import socket
import time
import json

sockTCP: socket.socket = None

def discover_bulb() -> dict | None:
  global sockTCP

  SSDP_ADDR = "239.255.255.250"
  SSDP_PORT = 1982
  SSDP_MX = 2
  SSDP_ST = "wifi_bulb"

  IPPROTO_UDP = 17
  IP_MULTICAST_TTL = 10
  # SSDP discovery message
  


  msg = f"""M-SEARCH * HTTP/1.1
  HOST: {SSDP_ADDR}:{SSDP_PORT}
  MAN: "ssdp:discover"
  ST: {SSDP_ST}
  MX: {SSDP_MX}

  """.replace("\n", "\r\n").encode()

  # Create UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, IPPROTO_UDP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.setsockopt(socket.IPPROTO_IP, IP_MULTICAST_TTL, 2)
  sock.settimeout(5)  # Set a timeout for receiving responses

  # Send the SSDP discovery message 4 wlan = network.WLAN(network.STA_IF)

  print(f"Sending SSDP discovery message: \n{msg.decode()}")
  sock.sendto(msg, (SSDP_ADDR, SSDP_PORT))

  # Listen for responses
  print("Listening for responses...")
  start_time = time.time()
  while time.time() - start_time < 5:  # Listen for 5 seconds
      try:
          data, addr = sock.recvfrom(1024)
          # print(f"\nResponse from {addr}:")
          responseDecoded = data.decode()
          responseParsed = parse_ssdp_response(responseDecoded)
          print(responseParsed["status"])

          host, port  = responseParsed["location"].split(":")
          sockTCP = _initSocketTCP(host, int(port))

          return responseParsed
      except socket.timeout:
          continue
    
  print("\nFinished listening for responses")
  sock.close()

  return None


""" 
SSDP response example
{
  "status": {
    "version": "HTTP/1.1",
    "code": 200,
    "message": "OK"
  },
  "cache_control": "max-age=3600",
  "date": "",
  "ext": "",
  "location": "192.168.3.156:55443",
  "server": "POSIX UPnP/1.0 YGLC/1",
  "id": "0x000000000eda65f5",
  "model": "colora",
  "fw_ver": "9",
  "support": "get_prop set_default set_power toggle set_bright set_scene cron_add cron_get cron_del start_cf stop_cf set_ct_abx adjust_ct set_name set_adjust adjust_bright adjust_color set_rgb set_hsv set_music udp_sess_new udp_sess_keep_alive udp_chroma_sess_new",
  "power": "on",
  "bright": 100,
  "color_mode": "2",
  "ct": 4000,
  "rgb": 16711680,
  "hue": 359,
  "sat": 100,
  "name": ""
}
 """
def parse_ssdp_response(response):
    lines = response.strip().split('\n')
    result = {}
    
    # Parse the status line
    if lines and lines[0].startswith('HTTP/'):
        status_parts = lines[0].split(' ', 2)
        result['status'] = {
            'version': status_parts[0],
            'code': int(status_parts[1]),
            'message': status_parts[2] if len(status_parts) > 2 else ''
        }
        lines = lines[1:]
    
    # Parse the headers and content
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower().replace('-', '_')
            value = value.strip()
            
            # Handle special cases
            if key == 'location' and value.startswith('yeelight://'):
                value = value[11:]  # Remove 'yeelight://' prefix
            elif key in ['power', 'bright', 'ct', 'rgb', 'hue', 'sat']:
                try:
                    value = int(value)
                except ValueError:
                    pass  # Keep as string if not convertible to int
            
            result[key] = value
        elif line.strip():
            # If there's content without a key, store it as 'content'
            result['content'] = result.get('content', '') + line + '\n'
    
    return result

def _initSocketTCP(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.settimeout(5)
    return sock

def _sendMessage(msg:dict):
    global sockTCP

    if sockTCP is None:
        return print("No socket TCP connection")
    
    data = json.dumps(msg)+ '\r\n'

    # send command
    sockTCP.sendall(data.encode('utf-8'))

    
    start_time = time.time()
    while time.time() - start_time < 5:  # Listen for 5 seconds
        # try:
        data, addr = sockTCP.recvfrom(1024)
        dataDecoded = data.decode()
        # print(f"\nResponse {dataDecoded}:")
        return json.loads(dataDecoded)
        """ except TimeoutError:
            continue """

def _setPower(state: str):
      
    msg = {'id': 1, 'method': 'set_power', 'params': [state, 'smooth', 500]}
    
    print(f"Attemptin turning {state}...")
    return _sendMessage(msg=msg)
    


def getPower():
    msg = {"id":1,"method":"get_prop","params":["power", "not_exist", "bright"]}
    print("Getting info of power... ",end="")
    res = _sendMessage(msg=msg)
    print(str(res["result"][0] == "on"))
    return res

def off():
    _setPower("off")

def on():
    _setPower("on")