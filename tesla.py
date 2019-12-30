#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from sys import stderr
ts = TouchSensor()
ir = InfraredSensor()
tankPair = MoveTank(OUTPUT_B, OUTPUT_C)

def top_left_channel_1_action(state):
    if state: # if state == True (pressed)
        tankPair.off() 
        exit()
    else:
        pass

print ("Starting....", file=stderr)
ir.on_channel1_top_left = top_left_channel_1_action
while True:
    try:
        tankPair.on(left_speed = 50, right_speed = 50) 
        if (ts.is_pressed == True) or (ir.proximity <= 25):
            tankPair.on_for_rotations(left_speed = -50, right_speed = -50, rotations=3)
            tankPair.on_for_degrees(left_speed = -50, right_speed = 50, degrees = 360)
    
        ir.process()
    except KeyboardInterrupt:
        tankPair.off()
        exit()
        break        
         