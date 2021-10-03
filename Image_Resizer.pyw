# Image resizing tool for Thingiverse
# This tool sizes the image to 

import os
import tkinter as tk
from PIL import Image
from tkinter.filedialog import askopenfilename

root = tk.Tk()
  
# specify size of window.
root.geometry("250x170")
  
# Create text widget and specify size.
T = tk.Text(root, height = 8, width = 52)
  
# Create label
T.pack()
T.insert(tk.END, "Welcome to image resizer!\nPlease choose image to resize:\n")
#tk.mainloop()

filename = askopenfilename()

image = Image.open(filename)

# The file format of the source file.
print('Format',image.format) # Output: JPEG

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print('Size in pixels:',image.size) # Output: (1920, 1280)

#Print size of image in kB
print('Size in kB:', os.path.getsize(filename)/1000)
txt = 'Size in kB: '+str(os.path.getsize(filename)/1000)+'\n'
T.insert(tk.END, txt)

# -------- Goal -> Reduce approx. 500 kB -----------
head, tail = os.path.split(filename)
print(tail)

newsize = 1000 # seed
counter = 1
imgqlty = 30;  # reduce to 30% in first attempt

while newsize > 500:
    newfilename = "cmpr_"+tail
    image.save(newfilename,optimize=True,quality=imgqlty)
    #image = Image.open(newfilename)
    newsize = os.path.getsize(newfilename)/1000
    print('New size in kB', newsize)
    counter = counter+1
    imgqlty = imgqlty-1

txt = 'New size in kB: '+str(os.path.getsize(newfilename)/1000)+'\n'
T.insert(tk.END, txt)    
print("Finished!")
T.insert(tk.END, "Finished!\n")
tk.mainloop()