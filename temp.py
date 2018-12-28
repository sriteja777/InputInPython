import sys
import os
import time
import tty

# os.close(sys.stdin.fileno())



import keyboard

tty.setraw(sys.stdin.fileno())

while True:
    if keyboard.is_pressed('a'):
        print('a pressed')
    if keyboard.is_pressed('s'):
        print('s pressed')
    if keyboard.is_pressed('q'):
        break
    # time.sleep(0.1)
