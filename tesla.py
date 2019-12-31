#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, MediumMotor, OUTPUT_A, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor, UltrasonicSensor
from sys import stderr
from time import sleep
from random import randint
ts = TouchSensor()
#ir = InfraredSensor()

ultra = UltrasonicSensor()
mediumMotor = MediumMotor(OUTPUT_A)
tankPair = MoveTank(OUTPUT_B, OUTPUT_C)

def backup(rot):
    tankPair.on_for_rotations(left_speed = -50, right_speed = -50, rotations=rot)

def moveForward(rot):
    tankPair.on_for_rotations(left_speed = 50, right_speed = 50, rotations=rot)

def turnLeft(rot):
    tankPair.on_for_rotations(left_speed = 50, right_speed = -50, rotations=rot)

def turnRight(rot):
    tankPair.on_for_rotations(left_speed = -50, right_speed = 50, rotations=rot)

def turnNeck(degrees):
    mediumMotor.on_for_degrees(speed=30, degrees = degrees)


print ("Starting....", file=stderr)

while True:
    try:
        tankPair.on(left_speed = 50, right_speed = 50) 
        if (ts.is_pressed == True):
            tankPair.off()    
            turnNeck(90)
            sleep(.5) 
            blockDistance = ultra.distance_centimeters
            print(blockDistance)
            if blockDistance > 100:
                print("GO!", file= stderr)
                turnNeck(-90)
                backup(1)
                turnLeft(1)

            else:
                turnNeck(-180)
                sleep(1)
                if ultra.distance_centimeters > 100:
                    turnNeck(90)
                    backup(1)
                    turnRight(1)  
                else:
                    turnNeck(90)
                    backup(2)
                    if randint(1,2) == 1:
                        turnRight(1)
                    else:
                        turnLeft(1)



                     
                    
                   

    except KeyboardInterrupt:
        tankPair.off()
        exit()
        break        
         