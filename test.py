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

try :
	x0,y0 = find_seed_global(f, c = 0.5)
except KeyError as e:
	print(e)
	
x = x0
y = y0

Liste_x = [x]
Liste_y = [y]

while x < 0.68 :
	x,y = Propagation(f, x, y, eps1, eps2, 0.5)
	Liste_x.append(x)
	Liste_y.append(y)
	
plt.figure()
plt.title(f" ligne de niveau associée à (x,y) -> x**2 + y**2 et 0.5")
plt.plot(Liste_x, Liste_y)
plt.show()

Liste_num = [(Liste_x[k],Liste_y[k]) for k in range(len(Liste_y))]
Liste_abscisse = [k for k in range(len(Liste_num))]
Liste_ordonnee = [(f(num[0],num[1])-0.5) for num in Liste_num]

plt.figure()
plt.title('résultat de la simulation')
plt.plot(Liste_abscisse, Liste_ordonnee)
plt.show() 