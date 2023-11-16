"""
This file contains callback functions for the bertec GUI.
Author: Jiefu Zhang
Date: 11/15/2020
"""
import winsound
import time

def speedIncrease(bertecObj):
    freq = 440
    dur = 500
    winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will speedup 
    time.sleep(0.5)

    speedL, speedR = bertecObj.get_belt_speed()
    # speedL = speedL + 0.1
    # speedR = speedR + 0.1
    # bertecObj._write_command(speedL, speedR) 

    print("Speed Increased, now: ", speedL, "m/s", end='\r')

def speedDrease(bertecObj):
    freq = 440
    dur = 500
    winsound.Beep(freq, dur)        # Just a beep sound to indicate the treadmill will slowdown
    time.sleep(0.5)
    speedL, speedR = bertecObj.get_belt_speed()
    # speedL = speedL + 0.1
    # speedR = speedR + 0.1
    # bertecObj._write_command(speedL, speedR) 

    print("Speed Decreased, now: ", speedL, "m/s", end='\r')


if __name__ == '__main__':
    winsound.Beep(440, 2000)
    print("You shouldn't run this file directly!")