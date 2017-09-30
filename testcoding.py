#!/usr/bin/python

from phue import Bridge
import logging
logging.basicConfig()
import time

b = Bridge('10.1.228.193')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

b.set_light(1,{'on': True,"hue":25500, "sat":255, "bri":255})
b.set_light(2,{'on': True,"hue":46920, "sat":255, "bri":255})
b.set_light(3,{'on': True,"hue":65280, "sat":255, "bri":255})


brightness = 0
while(1):
    brightness = 255 if brightness == 0 else 0
    b.set_light(1,{'transitiontime': 0, 'on': True, 'sat': brightness})
    time.sleep(0.5)

