# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:24:35 2019
load and display image with matplotlib to cnvert image to numpy array and back

@author: dina
"""

from matplotlib import image
from matplotlib import pyplot

#load image as pixel array
data = image.imread('personal0.jpg')

#data info
print('data type: ', data.dtype)
print('data shape ', data.shape)

#the array of pixels as an image
pyplot.imshow(data)
pyplot.show()

