import numpy as np
import matplotlib.pyplot as plt

def ligne_de_niveau(f,c,N1,N2,tolerance,iX = [-10,10],iY = [-10,10]):
    """renvoit un tableau de booléens tel que tab[i][j] est vrai ssi f(iX[0]+(iX[1]-iX[0])/N1,iY[0]+(iY[1]-iY[0)]/N2) est tolerance-proche de c
    qui représente les lignes de niveau c de la focntion f"""
    F = np.vectorize(f) 
    X = np.linspace(iX[0],iX[1],N1)
    Y = np.linspace(iY[0],iY[1],N2)
    tab = np.array([[[x,y] for y in Y] for x in X])
    tab = F(tab[:,:,0],tab[:,:,1])
    res = np.abs(tab - c*np.ones((N1,N2))) <= tolerance*np.ones((N1,N2)) 
    return res
    #plt.imshow(res)
    #plt.show()

#ligne_de_niveau(lambda x,y : np.cos(x**2 + y**2),0,1000,1000,0.01)
