import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
def f(x,y):
    return np.cos(x)**2 + np.sin(y)**2
X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
X,Y = np.meshgrid(X,Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,f(X,Y),cmap=cm.plasma)
plt.show()
