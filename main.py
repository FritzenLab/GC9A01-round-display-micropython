from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(4))
initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html

while True:
    try:
        currenttime= time.ticks_ms() #Every time it passes here, gets the current time
        if time.ticks_diff(time.ticks_ms(), initialtime) > 2000: # this IF will be true every 2000 ms
            initialtime= time.ticks_ms() #update with the "current" time

            # The DHT11 returns at most one measurement every 1s
            sensor.measure()
            # Retrieves measurements from the sensor
            print(f"Temperature : {sensor.temperature():.1f}")
            print(f"Humidity    : {sensor.humidity():.1f}")
            # Transmits the temperature to the computer console
    except OSError as e:
        print('Failed reception')
        # If the Pi Pico 2 does not receive the measurements from the sensor