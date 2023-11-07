# Importation de la librairie numpy

import numpy as np

# Utilisation de la fonction numpy.array()
arr = np.array([1, 2, 3]) # conversion d'une liste ou d'un objet en tableau grâce à la méthode np.array()

print (arr)
print (arr.ndim) # pour afficher le nombre de dimension
print (arr.size) # pour afficher la longueur

test1 = np.zeros((2, 3)) # tableau de 0 aux dimensions 2*3
test2 = np.ones((2, 3)) # tableau de 1 aux dimensions 2*3
print (test1)
print (test2)

test3 = np.random.randn(2, 3) # tableau aléatoire (distribution normale) aux dimensions 2*3
print (test3)

test4 = np.random.rand(2, 3) # tableau aléatoire (distribution uniforme)
print (test4)

test5 = np.random.randint(0, 10, [2, 3]) # tableau aléatoire de 0 à 10 et de dimension 2*3
print (test5)

print("------------------------------")
d = np.ones((2, 3), dtype=np.float16) # définit le type et la place à occuper sur la mémoire
print (d)
dat = np.linspace(1, 10, 10)
print (dat)
arran = np.arange(0, 10, 2)
print (arran)

print("------------------------------")

print(test1.shape)

# test1 = test1.reshape((3,2)) # redimensionne le tableau à 3 lignes et 2 colonnes
# print (test1)
# test1.ravel() # Aplatit le tableau à une seule dimension
# print (test1.ravel())

variable = np.concatenate((test1, test2), axis=0) # axe 0 : équivalent de np.vstack((test1, test2))
print(variable)
variable = np.concatenate((test1, test2), axis=1) # axe 1 : équivalent de np.hstack((test1, test2))
print(variable)
print(np.ones((1,1)))