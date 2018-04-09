#!/usr/bin/python
import os, time, sys, random, shutil
from subprocess import call

#See if there is the right amount of arguments
if len(sys.argv)==4:
    #Sets the wallpaper directory
    DIR = sys.argv[1]
    #Sets the pictuers desternation
    DST = sys.argv[2]
    #Sets the time to pause
    TIME = float(sys.argv[3])
    #Sets directory to the image directory
    os.chdir(DIR)
    #Waits till the time is set
    while True:
        time.sleep(TIME)
        #Selects a random image file
        FILE = random.choice(os.listdir(DIR))
        #Deletes the image in the pictuers distanation
        #os.remove(DST)
        #Copies the file
        shutil.copy2(FILE, DST)
        #Reseats i3wm
        call(["wal", "-c", "-i", DST, "-a ", sys.argv[4]])
        call(["feh", "--bg-scale", DST])
else:
    print("Please make sure that you have 3 arguments at the end of the command")
