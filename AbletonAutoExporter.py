import keyboard
import time
import subprocess
import os


# Prerequisites:
# Python3 installed
# keyboard module installed using the command
# 'pip install keyboard'
# in the PowerShell

for x in os.listdir():
    if x.endswith(".als"):

        #Opens the current .als file.
        temp = 'C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ./' + x
        subprocess.call(temp, shell=True)

        #The maximum time your projects will need to load into Ableton Live.
        #It is set to 60 seconds (1 minute) by default, change it according to your pc's performance.
        time.sleep(30) 

        #Executes the Export Audio/Video function and confirms all promps.
        keyboard.press_and_release("ctrl+shift+r")
        time.sleep(2)
        keyboard.press_and_release("enter")
        time.sleep(2)
        keyboard.press_and_release("enter")
        time.sleep(2)
        keyboard.press_and_release("enter")
        time.sleep(2)
        keyboard.press_and_release("enter")

        #The maximum time your projects will need to render completely.
        #It is set to 900 seconds (15 minutes) by default, change it according to your pc's performance.
        time.sleep(900)
