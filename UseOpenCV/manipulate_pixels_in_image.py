# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:12:07 2019

manipulate the pixels in an image

 OpenCV stores RGB channels in reverse order. While we normally think in terms 
 of Red, Green, and Blue, OpenCV actually stores them in the order of 
 Blue, Green, and Red. 
"""

from __future__ import print_function

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = " Path to the image")
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0,0]
print ("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
