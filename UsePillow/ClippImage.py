# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:08:33 2019
Cropp an image:  
    a piece can be cut out to create a new image, using the crop() function. 
The crop function takes a tuple argument that deﬁnes the two x and y 
  coordinates of the box to crop out of the image. 
For example, if the image is 1200x12000 pixels, we can clip out a 100x100 pixel
  box in the image. 
@author: dina
"""

from PIL import Image 
# load image 
image = Image.open('personal0.jpg') 
# create a cropped image 
cropped = image.crop((100, 100, 200, 200)) 
# show cropped image 
cropped.show()