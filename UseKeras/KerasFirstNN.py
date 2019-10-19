# -*- coding: utf-8 -*-
"""
in 
  Anaconda3\lib\ste-packages\keras\backend\tensorflow_backend.py
       line 422 change to
             variables = tf.compat.v1.global_variables()

Created on Sun Oct 13 04:35:44 2019
Use Keras to build first neural network.
The process is made of the stepd:
    - define the training data
    - define a neural network model
    - configure the learning process
    - train the model(iterate on the training data)
    
"""

#define training data
import numpy as np

# 2D tensors 
print("\ndefine data")
x_train = np.random.random((5000, 32))
y_train = np.random.random((5000, 5))


#define neural network model
print ("\ndefine neural network")
from keras import models
from keras import layers

INPUT_DIM = x_train.shape[1]

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_dim=INPUT_DIM))
model.add(layers.Dense(5, activation='softmax'))
# softmax activity function will return an array of 5 probability scores 
model.summary()


# configure learning process
#from keras import optimizers
#from keras import metrics

"""
* optimizer—The mechanism through which the network will update itself
            based on the data it sees and its loss function
* loss function—How the network will be able to measure its performance on
                the training data, and thus how it will be able to steer itself
                in the right direction
* metrics to monitor during training and testing—
                only care about accuracy (the fraction of the images that 
                were correctly classified).
"""
print ("\nconfigure learning process")
model.compile(optimizer='adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])


#train the model
"""
Have training data, have configured neural network to train with the data.
So do training process.
Training begins by calling the fit() method.

epochs = number of iterations
batch = the model don't process all the data at once 
        so break the data into small batches 
"""

print("\ntrain the model")
model.fit(x_train, y_train, epochs=10, batch_size=128)
