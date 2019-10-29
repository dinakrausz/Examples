# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:59:47 2019

load, display, save image

@author: dina
"""
from PIL import Image

#load image
#image = Image.open('Sydney opera house.jpg')
image = Image.open('personal0.jpg')

#print image details
print('image format: ', image.format)  #image format JPEG OR PNG
print('image mode: ', image.mode)      #pixel channel format (RGB or CMYK)
print('image size ', image.size)       #the dimention of the image in pixels

#show the image
image.show()


