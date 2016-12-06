# Run using sudo

import os
import time
import shutil
from textract import process
import pygame

pygame.mixer.init()
while True:
    print("On standby, please plug in 2 USB drives")
		pygame.mixer.music.load("standby.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
			
		pygame.mixer.music.stop()
    disks=os.system("ls /dev") # checks /dev for a disk
    if "sda1" in disks and "sda2" in disks:
        print("Two USB drives detected...")
		pygame.mixer.music.load("detected.mp3")
		pygame.mixer.music.play()
		
        # os.system("./usbcleaner.sh") may need to mount USB (see below)

        # THESE DIRECTORIES NEED TO BE REPLACED WITH WHERE WHATEVER DIRECTORY
        # THE USB HAS MOUNTED ON... if they aren't mounted, mount with script
        # above
        dir1="/mnt/usb"
        dir2="/mnt/usb"

        for subdir, dirs, files in os.walk(dir1): # loop through USB files
            for file in files:
                #print os.path.join(subdir, file)
                filepath = subdir + os.sep + file

                # if a file is a .pdf, convert to text before copying
                if filepath.endswith(".pdf"):
                    print("Detected dangerous file: " + filename)
                    #convert pdf to text with Textract
                    text = process(filename)
                    #save converted txt to DANGEROUS-tagged new file in 2nd usb
                    f = open(os.path.join(dir2,filename,'-DANGER'), 'w+')
                    f.write(text)
				elif filepath.endswith(".exe") or filepath.endswith(".msi"):
					print("Detected dangerous file: " + filename)
					f = open(os.path.join(dir2,filename,'-DANGER'), 'w+')
					f.write(text)
                else:
                    print("Copying clean file: " + filepath)

                    # THESE FILE PATH NAMES PROBABLY NEED TO BE FIXED
                    srcfile = os.path.join(dir1, filepath)
                    dest= os.path.join(dir2, filepath) #What is the point of this line?
					
                    # copy over file and directories if needed
                    assert not os.path.isabs(srcfile)
                    dest =  os.path.join(dstroot, os.path.dirname(srcfile))
                    os.makedirs(dstdir)
                    shutil.copy(srcfile, dstdir)
					
		pygame.mixer.music.load("done.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
			
		pygame.mixer.music.stop()
    time.sleep(0.5) # reset