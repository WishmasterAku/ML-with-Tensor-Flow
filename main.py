import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 

m = 2# Slope
b = 0.5# Intercept
x = np.linspace(0,4,100)# Create 100 points between 0 and 4
y = m * x + b + np.random.randn(*x.shape) * 0.5# Add some noise



plt.scatter(x,y)# Plot the data

class Model:
    def __init__(self):
        self.weight = tf.Variable(10)# Create a variable with an initial value of 10
        self.bias = tf.Variable(10)
        
    def __call__(self, x):# This is the function that will be called when we call the class
        return self.weight * x + self.bias
        #self.weight.assign_sub(15.0)
        
    