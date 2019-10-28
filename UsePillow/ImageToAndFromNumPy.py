# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:07:28 2019

load an image as a Pillow image object. 
Convert to a NumPy array. Convert NumPy array to an Image object
 
@author: dina
"""

from PIL import Image
from numpy import asarray

#load the image
image1 = Image.open('personal.jpg')

#convert image to numpy array
data = asarray(image1)
print(data.shape)

#print(data)

#create Pillow image
image2 = Image.fromarray(data)
#image details
print('\nimage format: ', image2.format)
print('image mode: ', image2.mode)
print('image size: ', image2.size)

