from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from tkinter.filedialog import askopenfilename


filename = askopenfilename()

photo = Image.open(filename)
    
#Store image width and height
w,h = photo.size
    

# make the image editable
drawing = ImageDraw.Draw(photo)
font = ImageFont.truetype("Roboto/Roboto-Black.ttf", 72)
# Download family of fonts from here: https://fonts.google.com/specimen/Roboto?selection.family=Roboto#standard-styles
    
#get text width and height
text = "© Your Name"
text_w, text_h = drawing.textsize(text, font)
    
pos = w - text_w, (h - text_h) - 60
    
c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
drawing = ImageDraw.Draw(c_text)
    
drawing.text((0,0), text, fill="#ffffff", font=font)
c_text.putalpha(100)
   
photo.paste(c_text, pos, c_text)
photo.save("trial.jpg")

