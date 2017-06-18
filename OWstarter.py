#!python3
'''OWstarter.py - a script to run overwatch
Only works for 1980 x 1080 screens
Please ensure that Overwatch Launcher.exe is found in C:\Program Files (x86)\Overwatch

Copyright (C) 2017 Chew Jing Wei

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''

import time
import os

import pyautogui as pag

if __name__ == '__main__':
    print("Running Script...")
    pag.click(1914, 1059) #show desktop
    with open('Config\\owlauncher.txt','r') as x:
        os.startfile(str(x.read())) #gets the path to the overwatch launcher executable and runs it
    while not pag.locateOnScreen("owload.png"):
        print("owload.png not found on screen yet..")
        time.sleep(3) #wait until the launcher loads up
    pag.click(1008, 527) #location for password field
    with open('Config\\password.txt','r') as f:
        pag.typewrite(str(f.read())) #get password from password.txt and type it in
    pag.click(1142, 604) #location for play button
    while not pag.locateOnScreen("OWplay.bmp"):
        print("OWplay.bmp not found on screen yet..")
        time.sleep(3) #wait until the play page loads up
    x, y = pag.locateCenterOnScreen("OWplay.bmp")
    pag.click(x, y) #location for play button after login
