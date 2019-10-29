# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:33:25 2019
To resize image dimantions use thumbnail() function.
The function takes a tuple with the height and width
 and the image will be resized so that the height and width of the image 
 are equal or smaller than the speciﬁed shape. 

Always  maintain the aspect ratio of the original image. 
@author: dina
"""

from PIL import Image

#load the image
image = Image.open('personal0.jpg') 
# print the size of the image 
print(image.size) 
# use thumbnail to change dimantions of the image
image.thumbnail((100,100)) 
# print the size of the modified image 
print(image.size) 
# show the image 
image.show()
