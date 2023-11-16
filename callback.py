"""
This file contains callback functions for the bertec GUI.
Author: Jiefu Zhang
Date: 11/15/2020
"""
import winsound
import time
from BertecMan_Mod import Bertec

# class Callback:
#     def __init__(self):
#         self.bertecObj = Bertec()
#         self.bertecObj.start()
#         print('Bertec communication set up')

#     def __exit__(self):
#         self.bertecObj.stop()
#         print('Bertec communication closed')

#     def speedIncrease(self):
#         freq = 800
#         dur = 1000
#         winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will speedup 
#         time.sleep(0.5)

#         speedL, speedR = self.bertecObj.get_belt_speed()         # TODO: The speed of bertec is not a constant
#         # speedL = speedL + 0.1
#         # speedR = speedR + 0.1
#         # self.bertecObj._write_command(speedL, speedR) 

#         print("Speed Increased, now: ", speedL, "m/s", end='\r')

#     def speedDecrease(self):
#         freq = 800
#         dur = 1000
#         winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will slowdown
#         time.sleep(0.5)
#         speedL, speedR = self.bertecObj.get_belt_speed()
#         # speedL = speedL + 0.1
#         # speedR = speedR + 0.1
#         # bertecObj._write_command(speedL, speedR) 

#         print("Speed Decreased, now: ", speedL, "m/s", end='\r')



def speedIncrease(bertecObj):
    freq = 800
    dur = 1000
    winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will speedup 
    time.sleep(0.5)

    speedL, speedR = bertecObj.get_belt_speed()         # TODO: The speed of bertec is not a constant
    speedAvg = (speedL + speedR) / 2
    speedL = speedAvg + 0.1
    speedR = speedAvg + 0.1
    bertecObj._write_command(speedL, speedR) 

    print("Speed Increased, now: ", speedL, "m/s", end='\r')

def speedDecrease(bertecObj):
    freq = 800
    dur = 1000
    winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will slowdown
    time.sleep(0.5)
    speedL, speedR = bertecObj.get_belt_speed()
    speedAvg = (speedL + speedR) / 2
    speedL = speedAvg - 0.1
    speedR = speedAvg - 0.1
    bertecObj._write_command(speedL, speedR) 

    print("Speed Decreased, now: ", speedL, "m/s", end='\r')


if __name__ == '__main__':
    winsound.Beep(440, 2000)
    print("You shouldn't run this file directly!")