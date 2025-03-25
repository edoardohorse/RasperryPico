from machine import Pin
import time

CLK = 0
DT= 1
SW = 3
STEP = 5
SCALE = 100

class RotaryEncoder:
    def __init__(self, pin_clk, pin_dt, pin_sw):
        self.pin_clk = Pin(pin_clk, Pin.IN, Pin.PULL_UP)
        self.pin_dt = Pin(pin_dt, Pin.IN, Pin.PULL_UP)
        self.pin_sw = Pin(pin_sw, Pin.IN, Pin.PULL_UP)
        
        self.clk_last_state = self.pin_clk.value()
        self.counter = 0
        self.direction = None
        self.button_pressed = False
        
        self.pin_clk.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.rotary_change)
        self.pin_sw.irq(trigger=Pin.IRQ_FALLING, handler=self.button_pressed_handler)

    def rotary_change(self, pin): 
        clk_state = self.pin_clk.value()
        dt_state = self.pin_dt.value()
        
        if clk_state != self.clk_last_state:
            if dt_state != clk_state:
                if self.counter - STEP < SCALE*-1: return
                self.counter -= STEP
                self.direction = "Counterclockwise"
            else:
                if self.counter + STEP > SCALE: return
                self.counter += STEP
                self.direction = "Clockwise"
            print(f"Counter: {self.counter}, Direction: {self.direction}")
        
        self.clk_last_state = clk_state

    def button_pressed_handler(self, pin):
        self.button_pressed = True
        print("Button pressed!")

    def get_counter(self):
        return self.counter

    def reset_counter(self):
        self.counter = 0

    def get_button_status(self):
        if self.button_pressed:
            self.button_pressed = False
            return True
        return False

# Initialize the rotary encoder
# Adjust these pin numbers according to your wiring
rotary = RotaryEncoder(pin_clk=CLK, pin_dt=DT, pin_sw=SW)

# Main loop
while True:
    if rotary.get_button_status():
        print("Button was pressed! Resetting counter.")
        rotary.reset_counter()
    
    time.sleep(0.1)  # Small delay to prevent excessive CPU usage