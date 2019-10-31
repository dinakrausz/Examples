# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:48:31 2019

 To maintain the pixel values in the positive domain, perhaps so the images can be
 visualized or perhaps for the beneﬁt of a chosen activation function in the 
 model. 
 A popular way of achieving this is to clip the standardized pixel values to 
 the range [-1, 1] and then rescale the values from [-1,1] to [0,1]. 
 
 The script updates the global standardization to demonstrate this additional
 rescaling.
 
@author: dina
"""

from numpy import asarray
from numpy import clip
from PIL import Image

# load image 
image = Image.open('opera_house0.jpg')
pixels = asarray(image) 
# convert from integers to floats 
pixels = pixels.astype('float32')

# calculate global mean and standard deviation 
mean, std = pixels.mean(), pixels.std()
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
# global standardization of pixels
pixels = (pixels - mean) / std 

# clip pixel values to [-1,1] 
pixels = clip(pixels, -1.0, 1.0) 
# from [-1,1] to [0,1] with 0.5 mean 
pixels = (pixels + 1.0) / 2.0 

# check it had the desired effect
mean, std = pixels.mean(), pixels.std() 
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std)) 
