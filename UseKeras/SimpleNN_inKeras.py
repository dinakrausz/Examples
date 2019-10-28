# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 06:05:06 2019
FROM   Deep Learning with Keras.pdf
           Antonio Gulli, Sujit Pal
use mnist database for train and test for digits recog
nition 
@author: dina
"""

import numpy as np

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils
import matplotlib.pyplot as plt


np.random.seed(1671) #for reproducibility

#network and training
NB_EPOCH = 200
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10 #number of outputs = number of digits
OPTIMIZER = SGD() #SGD optimizer
#N_HIDDEN = 128 #hidden neurons

VALIDATION_SPLIT=0.2 #how much TRAIN is reserved for VALIDATION

#data: shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#X_train is 60000 rows of 28x28=784(neurons) pixels --> reshaped in 60000x784
RESHAPED = 784

X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#normalize
X_train /= 255
X_test /= 255

print (X_train.shape[0], 'train samples')
print (X_test.shape[0], 'test samples')

#convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, NB_CLASSES)
Y_test = np_utils.to_categorical(y_test, NB_CLASSES)

# 10 outputs
# final stage is softmax
model = Sequential()
model.add(Dense(NB_CLASSES, input_shape=(RESHAPED,)))
# Softmax squashes a k-dimensional vector of arbitrary real values into a
#   k-dimensional vector of real values in the range (0, 1). 
#   In our case, it aggregates 10 answers provided by the previous layer with 10 neurons

model.add(Activation('softmax'))
model.summary()

model.compile(optimizer=OPTIMIZER, loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, Y_train, 
                    batch_size=BATCH_SIZE,
                    epochs=NB_EPOCH,
                    verbose=VERBOSE,
                    validation_split=VALIDATION_SPLIT)
                   
score = model.evaluate(X_test, Y_test, verbose=VERBOSE)

print("Test score: ", score[0])
print("test accuracy: ", score[1])

print ("Test score", history.history.keys())

#plot training and validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

#plot training and validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

