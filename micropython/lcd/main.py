from lcd_i2c import LCD
from machine import I2C, Pin
import time

# PCF8574 on 0x50
I2C_ADDR = 0x27    # DEC 39, HEX 0x27
NUM_ROWS = 2
NUM_COLS = 16

SDA = 4
SCL = 5

def init():
    # define custom I2C interface, default is 'I2C(0)'
    # check the docs of your device for further details and pin infos
    i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA), freq=400000)
    lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
    lcd.backlight()
    print("Has backlight?: "+str(lcd.get_backlight()))


    lcd.begin()
    lcd.print("Hello World")
    lcd.set_cursor(row=1, col=0)
    lcd.print("Hello World2")

def checkDisplay():
    i2c = I2C(0, sda=Pin(SDA), scl=Pin(SCL))
    print(i2c.scan())
    
if __name__ == "__main__":
    checkDisplay()
    init()
    