# -*- coding: utf-8 -*-
"""

GOOD ONLY FOR 3 INPUTS
create NN class to train the neuron to give an accurate prediction.
The problem:
                     input     output
    training data1   0  0  1    0
    training data2   1  1  1    1
    training data3   1  0  1    1
    training data4   0  1  1    0
    situation        1  0  0    ?
    
Train the NN to predict the correct output for new set of data.
Input: 3 binary numbers 
Output: close too 0 or close to 1 because use sigmoid activation function.

Note: 
    - use the derivative of sigmoid function to compute agjustments to the weights.
    - for output value "X" then the derivative is x *(1-x) 
    - use T function for transposing the matrix from horizontal position to
        vertical position

Training the model: (here teach the nn to make accurate prediction)
                     Every input will have positive or negative weight.
                     Big positive or negative weight will influence the 
                     resulting output more.
      
        Process:
            - take the inputs from the training dataset
            - perform adjustments based on their weights
            - use sigmoid function to compute the output of the ANN
            - compute the back propagated error rate: compute the difference 
                  between neuron's predicted output and 
                  the expected output of the training dataset. 
            - based on the value of the error rate, perform minor weight 
                  adjustments using the derivative formula
            - iterate this process 15000 times. In every iteration, the whole
                  training is processed simultaneously.
                  

@author: dina
"""

import numpy as np

class NN():
    
    def __init__(self):
        # seed for random numbers generator
        np.random.seed(1)
        
        # [3, 1] matrix that will contain float weights in range -1 to 1 
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1
        
    def sigmoid(self, x):
        #use sigmoid function
        return 1 / (1 + np.exp(-x))
        
    def sigmoid_derivative(self, x):
        # return derivative of sigmoid function
        return x * (1 - x)
    
    def train(self, training_inputs, training_outputs, training_iterations):
        #train the model to make accurate predictions while adjusting the weights
        
        for iteration in range(training_iterations):
            # train the data through the neuron
            output = self.think(training_inputs)
            
            #compute the error rate for back-propagation
            error = training_outputs - output
            
            #perform weight adgustments
            adjustments = np.dot(training_inputs.T, 
                                 error * self.sigmoid_derivative(output))
            
            self.synaptic_weights += adjustments
            
    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # convert values to float numbers
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output
    

def train(neural_network):
    print("\nbeginning random generated weights: ")
    print(neural_network.synaptic_weights)
    
    #training data consisting of 4 examples : 3 input values and 1 output value
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])
    #print("\ntraining inputs ", training_inputs)
    
    training_outputs = np.array([[0, 1, 1, 0]]).T
    #print("\ntraining inputs ", training_outputs)
    
    #do training
    neural_network.train(training_inputs, training_outputs, 15000)
    
    print('\n\nending weights after training: ')
    print(neural_network.synaptic_weights)
    
    
def main():
    # initialize the neuron class
    neural_network = NN()
    train(neural_network)
    
    user_input1 = input("User input one ")
    user_input2 = input("User input two ")
    user_input3 = input("User input three ")
    
    print('\nconsider new situation: ', user_input1, user_input2, user_input3)
    print('\nthe new output data ')
    print(neural_network.think(np.array([user_input1, user_input2, user_input3])))
    print('\n          The END ')

   
if __name__ == '__main__':
    main()


