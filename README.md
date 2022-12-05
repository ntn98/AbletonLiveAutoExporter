# AbletonLiveAutoExporter
A simple python script that allows you to export multiple Abeton Live sets automatically

# User Instructions

Prerequisites: 
- Windows
- python3 installed
- python keyboard module installed (can be done using the command 'pip install keyboard')

How To Use:

1. Download the AbletonLiveAutoExporter.py file

2. Create a folder containing all .als to be exported and place the script file in there.

3. Open the Windows Terminal in that folder by right-click -> open in Windows Terminal

4. Run the script via the command 'python AbletonLiveAutoExporter.py'

Things to note: 
- Make sure that the files have the right export settings before running the script
- Tracks will be exported with the name of the project file
- This script is very basic and can not handle if there already is a file with the same name at the target location
- By default the times to load an Ableton project and to export a track are set to 1 and 15 minutes, you can change this to fit your pc's performance by editing the script's file

# Disclaimer 
This script works by sending the keyboard inputs to export songs to ableton, it is not recommended to use the pc while the script is running.
