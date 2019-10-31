# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:40:10 2019
0<= pixel <= 255. 
Neural networks process inputs using small weight values, and inputs with large
 integer values can disrupt or slow down the learning process. 
So normalize the pixel values, each pixel value has a 0 <=value<=1.

@author: dina
"""

from numpy import asarray
from PIL import Image

#load image
image = Image.open('opera_house0.jpg')
pixels = asarray(image)

print('pixels')
print(pixels)

print('shape')
print(asarray(image).shape)
print('\n\nData Type: %s' % pixels.dtype)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

# convert from integers to floats
pixels = pixels.astype('float32')

# normalize to the range 0-1
pixels /= 255.0

#print the normalization
print('Normalized Min: %.3f, Normalized max: %.3f' % (pixels.min(), 
                                                      pixels.max()))


