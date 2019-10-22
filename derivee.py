import matplotlib.pyplot as plt
import numpy as np

def d1(f,a,h):
    """dérivée de f avec un schéma d'ordre 1"""
    return (f(a+h) - f(a))/h

def d2(f,a,h):
    """dérivée de f avec un schéma d'ordre 2"""
    return (f(a+h)-f(a-h))/(2*h)

def comparer(f,a,res):
    """compare les erreurs d'approximation de la dérivée de f en a de d1 et d2 pour différentes valeurs de h"""
    X = []
    L = [[],[]]
    for i in range(19):
        for k in range(1,10):
            h = k*10**(-i)
            X.append(h)
            L[0].append(np.abs(d1(f,a,h)-res)) 
            L[1].append(np.abs(d2(f,a,h)-res)) 


    ax = plt.gca()
    plt.xlabel("h")
    plt.ylabel("erreur")
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.plot(X,L[0],'.',label = "premier ordre")
    plt.plot(X,L[1],'.',label = "deuxième ordre") 
    plt.legend()
    plt.show()

x = 0
f = lambda x,y : np.cos(x)*np.sin(y)
def fy(y):
    return f(x,y)

comparer(np.exp,2,np.exp(2))



