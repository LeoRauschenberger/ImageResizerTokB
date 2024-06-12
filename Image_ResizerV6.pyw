#!/usr/bin/python3

# Image resizing tool for Thingiverse
# Author: Leo Rauschenberger
# This tool sizes the image to NO MORE THAN than the nbr. of kB you specify. Useful if you have a max. image size you are allowed to uplaod.


import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image
from tkinter.filedialog import askopenfilename

def restart_program():
    root.destroy()
    os.startfile("Image_ResizerV6.pyw")


#-------------------------------------------------------------------------------

root = Tk()
root.title('Image Resizer to kB')
  
# specify size of window.
root.geometry("410x200")

# for user Entry
def display_text():
    global entry
    string=  entry.get()
    label.configure(text=string)

# variable for "Enter" button press, it is 
button_pressed = StringVar()

l1 = Label(root, text="Desired size (kB): ")
l1.grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
#b1 =Button(root, text="Enter", command = display_text)
b1 = Button(root, text="Enter", command=lambda: button_pressed.set("button pressed"))
b1.grid(row=0, column=2)

# halting program till button press
b1.wait_variable(button_pressed)


imgkB = int(e1.get())
print("Desired size (kB): ",str(imgkB))

# Create text widget and specify size.
T = Text(root, height = 8, width = 52)
T.grid(row = 1, columnspan=3)
  
# Create label
T.insert(END, "Please browse for image to resize:\n")

filename = askopenfilename()

image = Image.open(filename)

# The file format of the source file.
print('Format',image.format) # Output: JPEG

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print('Size in pixels: ',image.size) # Output e.g.: (1920, 1280)
T.insert(END, 'Size in pixels: '+str(image.size)+'\n')

#Print size of image in kB
filesize = int(os.path.getsize(filename)/1000)
print('Size in kB:', filesize)
txt = 'Size in kB: '+str(filesize)+'\n'
T.insert(END, txt)

# -------- Goal -> Reduce approx. 500 kB -----------
head, tail = os.path.split(filename)
print(tail)

newsize = int(filesize) # seed
cntr = 1
resizefactor = 1.2

if newsize < imgkB:
    print("No action taken.")
    T.insert(END, "No action taken.\n")

while newsize > imgkB:
    newfilename = "cmpr_"+tail
    width, height = image.size
    newwidth = int(width/resizefactor)
    newheight = int(height/resizefactor)
    print("%.2f" % resizefactor, newwidth, newheight)
    im = image.resize((newwidth, newheight), resample=Image.ANTIALIAS)
    im.save(newfilename)
    newsize = int(os.path.getsize(newfilename)/1000)
    print('New size in kB:', newsize)
    cntr += 1
    resizefactor = resizefactor + 0.2

txt = 'New size in kB: '+str(newsize)+'\n'
T.insert(END, txt)    
print("Finished! Saved as", newfilename)
T.insert(END, "Finished! Saved as "+newfilename+"\n")

#Restart button
Button(root, text="Resize another image", command=restart_program).grid(row=2, column = 1)
root.mainloop()
