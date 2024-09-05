from machine import Pin, PWM
from time import sleep
import sys

# Initialize PWM for each color channel of an RGB LED
yellow = PWM(Pin(26))  # Red channel on GPIO pin 26
magenta = PWM(Pin(27))  # Green channel on GPIO pin 27
ciano = PWM(Pin(28))  # Blue channel on GPIO pin 28

# Set 1000 Hz frequency for all channels
yellow.freq(1000)
magenta.freq(1000)
ciano.freq(1000)

MAX = 65535

# Function to set RGB LED color
def set_color(c, m, y):
    ciano.duty_u16(c)  # Red intensity
    magenta.duty_u16(m)  # Green intensity
    yellow.duty_u16(y)  # Blue intensity


set_color(MAX, 0, 0)
sleep(1)
set_color(0, MAX, 0)
sleep(1)
set_color(0, 0, MAX)

sys.exit()

for i in range(0, MAX):
    set_color(i, i, i)  # Blue
    sleep(0.2)
    print(i)

try:
    while True:
        set_color(65535, 0, 0)  # Red
        sleep(1)
        set_color(0, 65535, 0)  # Green
        sleep(1)
        set_color(0, 0, 65535)  # Blue
        sleep(1)
        set_color(65530, 65530, 65530)  # Blue
        sleep(1)
        

except KeyboardInterrupt:
    set_color(0, 0, 0)  # Turn off RGB LED on interrupt