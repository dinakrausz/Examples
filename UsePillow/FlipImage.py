# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:56:26 2019
To flip image call flip() function. 
Use FLIP LEFT RIGHT for horizontal ﬂip, FLIP TOP BOTTOM for a vertical ﬂip. 
Other ﬂips are also available.

@author: dina
"""

from PIL import Image
from matplotlib import pyplot 

# load image
image = Image.open('personal0.jpg') 

# horizontal flip 
hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT) 

# vertical flip 
ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM) 

# plot all three images using matplotlib
pyplot.subplot(311) 
pyplot.imshow(image) 
pyplot.subplot(312)
pyplot.imshow(hoz_flip) 
pyplot.subplot(313)
pyplot.imshow(ver_flip)

