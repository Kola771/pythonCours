Cours de python 2

Il est mieux d'utiliser le PowerShell que le cmd pour éxécuter les codes pythons et faire les installations.

Ajouter à VSCode les extensions :
Python Extension Pack
Jupyter
Jupyter notebook

Pour éxécuter son code python, on peut faire :
- python le nom de votre fichier en étant dans le powershell ou dans un terminal (NB: Il faut être dans le dossier contenant le fichier)


L'indentation en python peut te coûter cher.
Elle est souvent utiliser en python pour des structures de codes.

Ou carrément utiliser un fichier Jupyter(.ipynb)


Les variables en python
- int
- float
- string
- bool

x = 3 # type int
y = 2.5 # type float
z = "hello" # type string
t = true # type boolean


Opération de comparaison et de logique en Python
AND
OR
^

Fonction en python
def nom_de_la_fonction(argument):
    ton code

ex:
def test():
    tester = 1 + 2
    return tester

test()#Energie potentiel
def e_potentielle(masse, hauteur, energie_limite, g=9.81):
  energie = masse  hauteur  g 
  print(energie)
  return energie > energie_limite

# ici g a une valeur par défaut donc nous ne sommes pas obligé de lui donner une valeur
e_potentielle(masse=10, hauteur=10,energie_limite=1000)


Les alternatives en Python
- If/Else
ex : 
def test_du_signe(valeur):
    if valeur < 0:
       print('négatif')
    elif valeur == 0:
       print('null')
    else: 
       print('positif')


Les Boucles en python
- For
Exemple :
Sans pas
for i in range(0, 10):
    print(i)
Avec pas
for i in range(0, 10, 2):
     print(i)
On peut pas faire de pas en float
Ce qu'on met dans pas (les sauts)

- While
Exemple :x = 5
while(x < 15):
    print(x)
    x += 1 # incrémentation de x à chaque boucle

a = 0
b = 1
i = 0
tab = [a, b]
while(i < 5):
    a, b = b, a+b
    tab.append(b)
    i += 1
print(tab)

def functionFinabocci(a, b, limit, x = 0):
    tab = [a, b]
    while x < limit :
        a, b = b, a+b
        tab.append(b)
        x += 1
    return tab

print(functionFinabocci(0, 1, 10))

def functionFinabocci0(a, b, limit):
    tab = [a, b]
    while b < limit :
        a, b = b, a+b
        tab.append(b)
    return tab

print(functionFinabocci0(0, 1, 10))


Listes et Tuples en python
Exemple de Liste: ex = [1,1]

Exemple de Tuples: ex = (1,2)

Une liste peut même conteniir des listes ! On appelle cela une nested Listvilles = ['Paris', 'Berlin', 'Londres', 'Bruxelles'] # liste initiale
print(villes)

villes.append('Dublin') # Rajoute un élément a la fin de la liste
print(villes)

villes.insert(2, 'Madrid') # Rajoute un élément a l'index indiqué
print(villes)

villes.extend(['Amsterdam', 'Rome']) # Rajoute une liste a la fin de notre liste
print(villes)

print('longeur de la liste:', len(villes)) #affiche la longueur de la liste

villes.sort(reverse=False) # trie la liste par ordre alphabétique / numérique
print(villes)

print(villes.count('Paris')) # compte le nombre de fois qu'un élément apparait dans la liste

def fibonacci(n):
    a=0
    b=1
    tab = [a, b]
    while b < n:
        a, b = b, a + b
        tab.append(b)
    return tab
print(fibonacci(7))


villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles'] # liste initiale
Afficher juste les éléments
for element in villes:
    print(element)

Récupérer les données et les index grâce à enumerate
for index, element in enumerate(villes):
    print(index, element)

Pour parcourir deux ou plusieurs tableaux
villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles'] # liste initiale
liste = [312, 52, 654, 23, 65, 12, 678]
for element_1, element_2 in zip(villes, liste):
    print(element_1, element_2)
La méthode zip prend en compte la longueur de la plus petite liste. Donc si j'ai deux listes de longueur 4 et 7, zip va juste prendre la longueur 4.


Les dicitonnaires en python# Dictionnaires
inventaire = {
    "pommes": 100,
    "bananes": 80,
    "poires": 120
}

# Récupération des clés du dictionnaire
print(inventaire.keys())
# Récupération des valeurs du dictionnaire
print(inventaire.values())
# Récupération de la longueur du dictionnaire
print(len(inventaire))