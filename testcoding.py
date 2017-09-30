#!/usr/bin/python

from phue import Bridge
import time

b = Bridge('10.1.228.193')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

b.set_light(1,{"hue":25500, "sat":255, "bri":255})
b.set_light(2,{"hue":46920, "sat":255, "bri":255})
b.set_light(3,{"hue":65280, "sat":255, "bri":255})


brightness = 250
while(1):
    brightness = 255 if brightness == 250 else 250
    b.set_light(1,{'transitiontime': 0, 'on': True, 'ct': brightness})
    time.sleep(0.5)