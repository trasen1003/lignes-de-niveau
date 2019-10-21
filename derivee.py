import matplotlib.pyplot as plt
import numpy as np

def d1(f,a,h):
    return (f(a+h) - f(a))/h

def dd(f,a,h,d):
    """dérivée de f avec une erreur en O(h^(d+1)) (sans prendre en compte l'erreur causée par les erreurs d'arrondies"""
    if d == 1:
        return d1(f,a,h)
    else:
         return (dd(f,a,h,d-1)+dd(f,a,(-h),d-1))/2

def comparer(f,a,d):
    """compare les erreurs d'approximation de la dérivée de f en a de dd pour différentes valeurs de d sur pour différentes valeurs de h"""
    X = []
    L = [[] for i in range(d)]
    for i in range(19):
        for k in range(10):
            h = k*10**(-i)
            X.append(h)
            for l in range(d):
                L[l].append(np.abs(dd(f,a,h,l+1)-f(a))) #f'(a) = f(a) pour l'exp, il faudrait utiliser autograd pour avoir une vraie valeur

    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    for l in range(d):
        plt.plot(X,L[l]) 
    plt.show()

comparer(np.exp,((2)),2)
