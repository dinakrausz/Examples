# -*- coding: utf-8 -*-
"""
use numpy to add, sub, mul, div  given matrix or vertex
"""

import numpy as np

x = np.array([[1, 2], [3, 4]])  
"""
x =  1   2
     3   4
"""

y = np.array([[5, 6], [7, 8]])
"""
y =   5  6
      7  8
""" 

# add the matices
a = x + y
"""
a= 6   8
   10  12
"""
print (" use +")
print (a)

print ("\n use add")
print (np.add(x, y))

"""
subtract:
    -4   -4
    -4   -4
"""
print ("\n use substract")
print (np.subtract(x, y))

"""
multiply:
   [[5   12]
    [21  32]]
"""
print ("\n elementwise multiplication")
print (np.multiply(x, y))


"""
division:
    [[0.2    0.33333333]
     [0.42857143  0.5]]
"""
print ("\n use division x/y")
print (np.divide(x, y))

"""
sum all numbers in x array
  10
"""
print ("\n sum all numbers in x array")
print (np.sum(x))


"""
sum numbers in each column of x array:
    [4  6]
"""
print ("\n sum numbers in each column of x array")
print (np.sum(x, axis = 0))


"""
sum numbers in each row of y array:
    [11  15]
"""
print ("\n sum numbers in each row of y array")
print (np.sum(y, axis = 1))



