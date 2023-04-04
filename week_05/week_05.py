import numpy as np
import math
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2)) / np.sqrt(x ** 2 + y ** 2)

x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize =(14,6))
ax = fig.add_subplot(1,2,1,projection='3d')

ax.contour(X, Y, Z, 75)

plt.show()

#----------------------------------------------

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2)) / np.sqrt(x ** 2 + y ** 2)

x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.contour(X, Y, Z, 50)

plt.show()