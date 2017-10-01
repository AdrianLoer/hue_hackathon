#!/usr/bin/python

from phue import Bridge
from rgbxy import Converter
import logging
import sys

logging.basicConfig()
import time
import datetime

tick = datetime.timedelta(milliseconds=250)
converter = Converter()
red = converter.rgb_to_xy(255, 0, 0)
blue = converter.rgb_to_xy(0, 0, 255)
green = converter.rgb_to_xy(0, 255, 0)
purple = converter.rgb_to_xy(180, 14, 184)
orange = converter.rgb_to_xy(196, 65, 5)

scenes = {"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}
groupid = 1

def get_lightstate(light_no, on):
    if light_no == 1:
        color = green
    elif light_no == 2:
        color = blue
    else:
        color = red
    return {
        'xy': color,
        'on': on,
        'transitiontime': 0
    } if on else {
        'on': False,
        'transitiontime': 0
    }


def init_scenes(bridge):
    for scene in b.scenes:
        b.request(mode='DELETE', address='/api/' + b.username + '/scenes/' + scene.scene_id)
    bridge.set_light(1, {'on': False, 'transitiontime': 0})
    bridge.set_light(2, {"on": False, 'transitiontime': 0})
    bridge.set_light(3, {'on': False, 'transitiontime': 0})
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
    bridge.set_light(1, {'xy': purple, 'on':True, 'transitiontime': 0})
    bridge.set_light(2, {'xy': purple, 'on': True, 'transitiontime': 0})
    bridge.set_light(3, {'xy': purple, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/',
                   data={'name': 'xxx', 'lights': ['1', '2', '3'], 'recycle': True})
    bridge.set_light(1, {'xy': orange, 'on':True, 'transitiontime': 0})
    bridge.set_light(2, {'xy': orange, 'on': True, 'transitiontime': 0})
    bridge.set_light(3, {'xy': orange, 'on': True, 'transitiontime': 0})
    bridge.request(mode='POST', address='/api/' + bridge.username + '/scenes/',
                   data={'name': 'yyy', 'lights': ['1', '2', '3'], 'recycle': True})
    #bridge.set_light(1, {'hue': })
    for scene in bridge.scenes:
        if scene.name in scenes.keys():
            one = True if scene.name[0] == '1' else False
            two = True if scene.name[1] == '1' else False
            three = True if scene.name[2] == '1' else False
            bridge.request(mode='PUT', address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/1', data=get_lightstate(1, one))
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/2',
                           data=get_lightstate(2, two))
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/3',
                           data=get_lightstate(3, three))
        if scene.name == 'xxx':
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/1',
                           data={'xy': purple, 'on': True, 'transitiontime': 0})
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/2',
                           data={'xy': purple, 'on': True, 'transitiontime': 0})
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/3',
                           data={'xy': purple, 'on': True, 'transitiontime': 0})
        if scene.name == 'yyy':
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/1',
                           data={'xy': orange, 'on': True, 'transitiontime': 0})
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/2',
                           data={'xy': orange, 'on': True, 'transitiontime': 0})
            bridge.request(mode='PUT',
                           address='/api/' + bridge.username + '/scenes/' + scene.scene_id + '/lightstates/3',
                           data={'xy': orange, 'on': True, 'transitiontime': 0})


def do_clocked(bridge, scene_id):
    start = datetime.datetime.now()
    bridge.request(mode='PUT', address='/api/' + bridge.username + '/groups/0/action',
                   data={'scene': scene_id, 'transitiontime': 0})
    end = datetime.datetime.now()
    elapsed = end - start
    wait_for = tick - elapsed
    time.sleep(wait_for.total_seconds())


def say_nrz(bridge, data, lights):
    sent = 0
    length = len(data)
    stuffing = length % len(lights)
    stuff = [0] * stuffing
    data = stuff + data
    length += stuffing
    start_id = 0
    for scene in bridge.scenes:
        if scene.name in scenes.keys():
            scenes[scene.name] = scene.scene_id
        if scene.name == 'xxx':
            delim_id = scene.scene_id
        if scene.name == 'yyy':
            start_id = scene.scene_id
    do_clocked(bridge, start_id) #start sequence
    while sent < length:
        scene_id = scenes[(''.join([str(x) for x in data[sent:sent + 3]]))]
        do_clocked(bridge, scene_id)
        sent += 3
    do_clocked(bridge, delim_id) #end sequence



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


if len(sys.argv) > 1:
    words = ' '.join(sys.argv[1:])
    chars = [bin(ord(x)) for x in words]
    byte_list = [int(digit[2:]) for digit in chars]
    accu = []
    for s in byte_list:
        accu.extend(str(s))
    accu = [int(x) for x in accu]
    say_nrz(b, accu, [1, 2, 3])
else:
    say_nrz(b, [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 2, 3])
#init_scenes(b)

