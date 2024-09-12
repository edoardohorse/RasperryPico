import machine
import utime

# Imposta il pin del pulsante (adatta al tuo circuito)
button_pin = 17

led = machine.Pin("LED", machine.Pin.OUT)


# Imposta il pin come ingresso con pull-down
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Opzionale: imposta il pin del LED come uscita
# led = machine.Pin(led_pin, machine.Pin.OUT)

while True:
    # print(button.value())
    if button.value() == 0:
        # print("Pulsante premuto")
        led.on()
    else:
        # print("Pulsante rilasciato")
        led.off()

    utime.sleep_ms(100)