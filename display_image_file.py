#!/usr/bin/env python3
from ev3dev2.display import Display
from time import sleep
from PIL import Image

lcd = Display()

logo = Image.open('/home/robot/pics/Bomb.bmp')
lcd.image.paste(logo, (0,0))
lcd.update()
sleep(5)
