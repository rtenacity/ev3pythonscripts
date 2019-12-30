#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.led import Leds
from sys import stderr
from time import sleep

cl=ColorSensor()

ts = TouchSensor()

# Put the color sensor into COL-COLOR mode.
cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')
while not ts.value():    # Stop program by pressing touch sensor button
    print(colors[cl.value()], file=stderr)
    #Sound.speak(colors[cl.value()]).wait()
    sleep(1)
Sound.beep()