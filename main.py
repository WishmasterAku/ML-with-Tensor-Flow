import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 

m = 2
b = 0.5
x = np.linspace(0,4,100)
y = m * x + b + np.random.randn(*x.shape) * 0.5

plt.scatter(x,y)