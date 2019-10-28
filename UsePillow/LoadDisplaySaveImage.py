# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:59:47 2019

load, display, save image

@author: dina
"""
from PIL import Image

#load image
#image = Image.open('opera_house.jpg')
image = Image.open('personal.jpg')

#print image details
print('image format: ', image.format)
print('image mode: ', image.mode)
print('image size ', image.size)

#show the image
image.show()


