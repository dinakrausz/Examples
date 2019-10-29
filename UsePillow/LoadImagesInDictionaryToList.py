# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:59:50 2019
load all images in a dictionary and put them in a list
 
@author: dina
"""

#Load all images in a dictionary.Here images dictionary and my scripts that use
#Pillow in same dictionary

from os import listdir
from matplotlib import image

# load all images in a directory and put them in a list 
#  all the images in 'images' dictionary
loaded_images = list() 
for filename in listdir('images'):
    #load one image
    one_image_data = image.imread('images/' + filename)
    #store loaded image in the list
    loaded_images.append(one_image_data)
    print('  loaded %s  %s' % (filename, one_image_data.shape))
    
