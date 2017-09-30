#!/usr/bin/python

from phue import Bridge
import logging

logging.basicConfig()
import time
import datetime

tick = datetime.timedelta(milliseconds=500)

scenes = {"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}
groupid = 1

def init_scenes(bridge):
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": False, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '000', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": False, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '001', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": True, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '010', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": True, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '011', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": False, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '100', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": False, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '101', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": True, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': False, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '110', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": True, 'transitiontime': 0})
    bridge.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/', data={'name': '111', 'lights': ['1', '2', '3'], 'recycle': True})


def say_nrz(bridge, data, lights):
    sent = 0
    length = len(data)
    stuffing = length % len(lights)
    stuff = [0] * stuffing
    data = stuff + data
    length += stuffing
    for scene in bridge.scenes:
        if scene.name in scenes.keys():
            scenes[scene.name] = scene.scene_id
    while sent < length:
        start = datetime.datetime.now()
        scene_id = scenes[(''.join([str(x) for x in data[sent:sent + 3]]))]
        bridge.activate_scene(groupid, scene_id)
        sent += 3
        end = datetime.datetime.now()
        elapsed = end - start
        wait_for = tick - elapsed
        time.sleep(wait_for.total_seconds())


b = Bridge('10.1.228.193')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

b.set_light(1, {"hue": 25500, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
b.set_light(2, {"hue": 46920, "sat": 255, "bri": 255, "on": True, 'transitiontime': 0})
b.set_light(3, {"hue": 65280, "sat": 255, "bri": 255, 'on': True, 'transitiontime': 0})
time.sleep(1)

b.set_group(groupid, 'lights', [1,2,3])

# brightness = 250
# while(1):
# brightness = 255 if brightness == 250 else 250
# b.set_light(1,{'transitiontime': 0, 'on': True, 'hue': brightness})
# time.sleep(0.5)

say_nrz(b, [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 2, 3])
#init_scenes(b)