import machine
import time

# Imposta il pin del pulsante (adatta al tuo circuito)
button_pin = 17

led = machine.Pin("LED", machine.Pin.OUT)

# Imposta il pin come ingresso con pull-down
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Opzionale: imposta il pin del LED come uscita
# led = machine.Pin(led_pin, machine.Pin.OUT)

# Function to handle button press down
def button_pressed():
    print("Button pressed!")
    # Add your desired actions here


# Main loop
while True:
    if button.value() == 0:
        button_pressed()
        while button.value() == 0:
            time.sleep(0.01)  # Debounce delay
