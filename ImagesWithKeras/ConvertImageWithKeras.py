# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:25:53 2019

 Use Keras img_to_array() function to convert a loaded image in PIL format 
   into a Numpy array (for deep learning models).
   
   Use Keras  array to img() function to convert a Numpy array of pixels data
   into a PIL image. 
   
   In the example, load image, convert it to a Numpy array and then convert the
   array back into a PIL image
   
@author: dina
"""

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img 
 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "Path to the image")
args = vars(ap.parse_args())

#load image
img = load_img(args['image'])
print("\img type ", type(img))

#convert image to numpy array
img_array = img_to_array(img) 
print("\narray type ", img_array.dtype)
print("\narray shape ", img_array.shape) 

# convert back to image
img_pil = array_to_img(img_array)
print("\n\nimg from numpy array type ", type(img_pil))


