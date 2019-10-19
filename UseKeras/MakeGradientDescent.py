# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:58:59 2019
gradient descent of the functions:
    - f(x) = (x+5)^2
    - f(x) = (-x+5)^2 * (x+3)^2
 
@author: dina
"""

def f1():
    """
    optimization algorithm to find the minimum of the function starting from 
    the point x=3
    
    f(x) = (x+5)^2
    gradient: 2(x+5)
    x0 = 3
    learning rate = 0.01
    num iterations = 10000        
    """
    
    # Initialize parameters
    cur_x = 3 # The algorithm starts at x=3
    rate = 0.01 # Learning rate
    precision = 0.000001 #This tells us when to stop the algorithm
    previous_step_size = 1 #
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    
    df = lambda x: 2*(x+5) #Gradient of our function 

    while previous_step_size > precision and iters < max_iters:
        prev_x = cur_x
        cur_x = cur_x - rate * df(prev_x) #Grad descent
        previous_step_size = abs(cur_x - prev_x) #Change in x
        iters = iters+1 
        print("Iteration",iters,"\n    X = ",cur_x) 
    
    print("The local minimum occurs at", cur_x)

    
def f2(x):
    """
    optimization algorithm to find the minimum of the function starting from 
    the point x
    
    f(x) = (-x+5)^2 * (x+3)^2
    gradient: 4*(-x+5)*(x+3)*(-x+1)
      minimum at x=5  or x = -3
    learning rate = 0.01
    num iterations = 10000        
    """    
    
    # Initialize parameters
    cur_x = x # The algorithm starts at x=30
    rate = 0.01 # Learning rate
    precision = 0.000001 #This tells us when to stop the algorithm
    previous_step_size = 1 #
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    
    df = lambda x: 4*(-x+5)*(x+3)*(-x+1) #Gradient of our function 

    while previous_step_size > precision and iters < max_iters:
        prev_x = cur_x         
        cur_x = cur_x - rate * df(prev_x) #Grad descent
        previous_step_size = abs(cur_x - prev_x) #Change in x
        iters = iters+1 
        print("Iteration",iters,"\n    X = ",cur_x) 
        if (abs(cur_x)>100000000):            
            return None    
    return cur_x


def main():
    import random
  
    while True:
        x = random.randint(-30, 30)       
        min_x = f2(x)
        if (min_x != None):
            print("The local minimum occurs at", min_x)
            break
        else:
            print("start point ", x, "not good so try again\n")
    

if __name__=='__main__':
    main()
