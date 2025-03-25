## Debuggin with Mosquitto

### Publish (set state)
```sh
# To led on
.\mosquitto_pub.exe -h 192.168.1.49 -t "pico/led" -m 1 -u mqtt_user -P Jkd882HnjrqECH

# To led off
.\mosquitto_pub.exe -h 192.168.1.49 -t "pico/led" -m 0 -u mqtt_user -P Jkd882HnjrqECH
```

### Subscribe (get state)
 

 ```sh
# Update state when switch change
.\mosquitto_sub.exe -h 192.168.1.49 -t "pico/led/state" -u mqtt_user -P Jkd882HnjrqECH

```