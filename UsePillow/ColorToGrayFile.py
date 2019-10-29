# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:24:23 2019

Script that  converting color images (RGB channels) to grayscale (1 channel)
Pillow use the convert() function and the mode ‘L’ will convert an image
 to grayscale.
 
Save a grayscale version of a loaded image 

@author: dina
"""

from PIL import Image 
# load the image 
image = Image.open('personal0.jpg') 
# convert the image to grayscale 
gs_image = image.convert(mode='L') 
# save in jpeg format 
gs_image.save('personal_grayscale0.jpg') 
# load the gray image and show it 
image2 = Image.open('personal_grayscale0.jpg') 
# show the image 
image2.show()

