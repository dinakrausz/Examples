# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:50:28 2019
Force the pixels into a new shape. 
Use resize() function that allows to specify the width and height in pixels
so the image will be reduced or stretched to ﬁt the new shape
@author: dina
"""

from PIL import Image 
# load the image 
image = Image.open('personal0.jpg') 
# print the size of the image 
print(image.size) 
# resize image so ignore original aspect ratio
img_resized = image.resize((400,400)) 
# print the size of the thumbnail 
print(img_resized.size) 
# show the image 
img_resized.show()

