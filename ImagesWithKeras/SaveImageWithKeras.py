# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:55:38 2019

 Keras API save img() function to save an image to ﬁle. 
 The function takes the path to save the image and the image data in NumPy 
 array format.
 The ﬁle format is inferred from the ﬁlename but can also be speciﬁed via the
 file format argument. 
 
 The example below loads the photograph image in grayscale format, converts it
 to a NumPy array, and saves it to a new ﬁle name.

@author: dina
"""

from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array 

#load image
img = load_img('bondi_beach.jpg', color_mode='grayscale')

# convert image to a numpy array 
img_array = img_to_array(img)

# save the image with a new filename 
save_img('bondi_beach_grayscale.jpg', img_array) 

# load the image to confirm it was saved correctly 
img = load_img('bondi_beach_grayscale.jpg') 
#print image details
print(type(img))
print('image format: ', img.format)  #image format JPEG OR PNG
print('image mode: ', img.mode)      #pixel channel format (RGB or CMYK)
print('image size ', img.size)       #the dimention of the image in pixels

img.show()

