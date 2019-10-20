## Modules utilisés

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

## Fonction de test et constantes

def f(x,y):
	return x**2 + y**2

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


affiche_ligne(f, np.linspace(0.5,1.1,4), [-2,2], [-2,2], eps1, eps2)
#Liste_num = [(Liste_x[k],Liste_y[k]) for k in range(len(Liste_y))]
#Liste_abscisse = [k for k in range(len(Liste_num))]
#Liste_ordonnee = [(f(num[0],num[1])-0.5) for num in Liste_num]

#plt.figure()
#plt.title('résultat de la simulation')
#plt.plot(Liste_abscisse, Liste_ordonnee)
# plt.show() 