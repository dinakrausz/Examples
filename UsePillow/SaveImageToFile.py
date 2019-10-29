# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:12:32 2019
Save images to file. 
Use it if want to save the image in different format such as PNG, GIF, PEG
In this script, load image in JPEG format and save in PNG format 
in same dictionary 
@author: dina
"""

from PIL import Image

#load the image
image = Image.open('personal0.jpg')

#save as PNG format
image.save('personal.png', format='PNG')
print(image.format)

#load the image.png and inspect the format 
image2 = Image.open('personal.png') 
print(image2.format)





