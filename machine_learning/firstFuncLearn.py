import numpy as np

def initialisation(m, n):
    X = np.random.randint(0, 10, [m, n+1])
    myMatrice = np.concatenate((X, np.ones((m, 1))), axis=1) # j'utilise le concatenate horizontal
    return myMatrice
print (initialisation(2, 1))
print (initialisation(4, 3))