# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 06:37:03 2019
   
@author: dina
"""

from keras.preprocessing.image import load_img
 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "Path to the image")
args = vars(ap.parse_args())

#load image
img = load_img(args['image'])

#print image details
print(type(img))
print('image format: ', img.format)  #image format JPEG OR PNG
print('image mode: ', img.mode)      #pixel channel format (RGB or CMYK)
print('image size ', img.size)       #the dimention of the image in pixels

#show the image
img.show()
