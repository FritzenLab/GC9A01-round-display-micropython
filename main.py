from machine import Pin, SPI
import gc9a01py as gc9a01
from machine import I2C
import time
import dht
from hdc1080 import HDC1080

i2c = I2C(0)
hdc = HDC1080(i2c)

    
initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html
hdc.config(humid_res=14, temp_res=14, mode=0, heater=0)

if hdc.check():
    print(f"Found HDC1080 with serial number {hdc.serial_number()}")
    
def main():
    
    spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(20, Pin.OUT),
        cs=Pin(21, Pin.OUT),
        reset=Pin(22, Pin.OUT),
        backlight=Pin(1, Pin.OUT),
        rotation=90)
    
    tft.fill(gc9a01.GREEN)
    initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html
    sensor = dht.DHT11(Pin(15))
    
    # from fonts import vga1_8x8 as font
    from fonts import vga2_8x8 as font1
    # from fonts import vga1_8x16 as font
    from fonts import vga2_8x16 as font2
    # from fonts import vga1_16x16 as font
    # from fonts import vga1_bold_16x16 as font
    # from fonts import vga2_16x16 as font
    from fonts import vga2_bold_16x16 as font3
    # from fonts import vga1_16x32 as font
    # from fonts import vga1_bold_16x32 as font
    # from fonts import vga2_16x32 as font
    from fonts import vga2_bold_16x32 as font

    while True:
        try:
            currenttime= time.ticks_ms() #Every time it passes here, gets the current time
            if time.ticks_diff(time.ticks_ms(), initialtime) > 3000: # this IF will be true every 2000 ms
                initialtime= time.ticks_ms() #update with the "current" time

                print(f"{hdc.temperature()} C, {hdc.humidity()} RH")
                temp1= str(round(hdc.temperature(),2))
                hum1= str(round(hdc.humidity(),2))
                tft.text(font3, "HDC1080", 70, 40, gc9a01.BLACK, gc9a01.GREEN)
                tft.text(font3, "sensor", 70, 60, gc9a01.BLACK, gc9a01.GREEN)
                tft.text(font, "Temperature:", 30, 80, gc9a01.WHITE, gc9a01.GREEN)
                tft.text(font, temp1, 70, 120, gc9a01.WHITE, gc9a01.GREEN)
                tft.text(font, " C", 150, 120, gc9a01.WHITE, gc9a01.GREEN)
                tft.text(font2, "Humidity:", 80, 160, gc9a01.BLACK, gc9a01.GREEN)
                tft.text(font2, hum1, 100, 180, gc9a01.BLACK, gc9a01.GREEN)
                tft.text(font2, " %", 140, 180, gc9a01.BLACK, gc9a01.GREEN)

        except OSError as e:
            print('Failed reception')
            # If the Pi Pico 2 does not receive the measurements from the sensor 


main()