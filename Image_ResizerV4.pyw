#!/usr/bin/python3

# Image resizing tool for Thingiverse
# This tool sizes the image to 

import os
import sys
from tkinter import *
from tkinter import *
from tkinter.ttk import *
from PIL import Image
from tkinter.filedialog import askopenfilename

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#-------------------------------------------------------------------------------

root = Tk()
root.title('Image Resizer to kB')
  
# specify size of window.
root.geometry("500x200")
  

Label(root, text="Desired Size").grid(row=0)
email = StringVar()
e1 = Entry(root,width=30, textvariable=email)
e1.grid(row = 0, column = 1, sticky = W, pady = 2)
e1.focus_set()

tx =e1.get()
print(str(tx))

# Create text widget and specify size.
T = Text(root, height = 8, width = 52)
T.grid(row = 1, column = 1)

#Restart button
Button(root, text="Resize another image", command=restart_program).grid(row=2, column = 1)
  
# Create label
T.insert(END, "--Welcome to image resizer!--\nPlease choose image to resize:\n")

filename = askopenfilename()

image = Image.open(filename)

# The file format of the source file.
print('Format',image.format) # Output: JPEG

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print('Size in pixels:',image.size) # Output: (1920, 1280)

#Print size of image in kB
filesize = int(os.path.getsize(filename)/1000)
print('Size in kB:', filesize)
txt = 'Size in kB: '+str(filesize)+'\n'
T.insert(END, txt)

# -------- Goal -> Reduce approx. 500 kB -----------
head, tail = os.path.split(filename)
print(tail)

newsize = int(filesize) # seed
counter = 1
#qltyfactor = int(180000/filesize)
#imgqlty = qltyfactor; #varies depending on inital filesize
#imgqlty = 30;  # reduce to 30% in first attempt
resizefactor = 1.2

if newsize < 500:
    print("No action taken.")

while newsize > 500:
    newfilename = "cmpr_"+tail
    #image.save(newfilename,optimize=True,quality=imgqlty)
    width, height = image.size
    newwidth = int(width/resizefactor)
    newheight = int(height/resizefactor)
    print("%.2f" % resizefactor, newwidth, newheight)
    im = image.resize((newwidth, newheight), resample=Image.ANTIALIAS)
    im.save(newfilename)
    #image = Image.open(newfilename)
    newsize = int(os.path.getsize(newfilename)/1000)
    print('New size in kB:', newsize)
    counter = counter+1
    #imgqlty = imgqlty-1
    resizefactor = resizefactor + 0.2

txt = 'New size in kB: '+str(newsize)+'\n'
T.insert(END, txt)    
print("Finished!")
T.insert(END, "Finished!\n")


mainloop()
