# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:25:58 2019

Note: distribution of pixel values often follows Gaussian distribution 
Calculate the mean and standard deviations across all color channels in the 
 loaded image, then uses these values to standardize the pixel values

@author: dina
"""

from numpy import asarray
from PIL import Image

# load image
image = Image.open('opera_house0.jpg')
pixels = asarray(image) 
pixels = pixels.astype('float32')

# calculate global mean and standard deviation 
mean, std = pixels.mean(), pixels.std()
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std)) 

# global standardization of pixels
pixels = (pixels - mean) / std 
# confirm it had the desired effect
mean, std = pixels.mean(), pixels.std()
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
