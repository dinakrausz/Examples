# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:41:10 20
USE OpenCV
   first script
load display save image 
"""

from __future__ import print_function

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = " Path to the image")
args = vars(ap.parse_args())

# parse the arguments and store them in a dictionary
image = cv2.imread(args["image"])

print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)

#save the image with new name
cv2.imwrite("newimage.jpg", image)


