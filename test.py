## Modules utilisés

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import *
import time
## Fonction de test et constantes

def f(x,y):
	return cos(x**2 + y**2)
	
def g(x,y):
	return x**2 + y**2
	
def h(x,y):
	return x*y
	
def i(x,y):
	return cos(x)*sin(y)

def j(x,y):
	return sin(x)/y

eps1 = 10 ** -2
eps2 = 10 ** -5

## Affichage de f

# X = np.linspace(0,1,500)
# Y = np.linspace(0,1,500)
# X,Y = np.meshgrid(X,Y)
# 
# Z = f(X,Y)
# 
# 
# fig = plt.figure()
# ax = Axes3D(fig)
# 
# ax.plot_surface(X,Y,Z,cmap = 'hot')
# 
# plt.show() 


## test des fonctions


affiche_ligne(j, [1], [-5,5], [0.01,1.1], eps1, eps2)
#Liste_num = [(Liste_x[k],Liste_y[k]) for k in range(len(Liste_y))]
#Liste_abscisse = [k for k in range(len(Liste_num))]
#Liste_ordonnee = [(f(num[0],num[1])-0.5) for num in Liste_num]

#plt.figure()
#plt.title('résultat de la simulation')
#plt.plot(Liste_abscisse, Liste_ordonnee)
# plt.show() 