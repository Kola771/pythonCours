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


Les list comprehension permettent de faire des déclarations sur une même ligne et de réduire le temps de calculs de python avec des syntaxes courtes
%%time
listes = [i**2 for i in range(100000)]

%%time
dico = {i: i**2 for i in range(20)}

** c'est pour faire l'exponentiel d'un nombre par exemple
2² (2*2) ou 2*2*2 (2**3)

# Built-in function
- fonction de bases :
abs(), round(), max(), min(), len(), sum(), any(), all(),
round() : C'est pour l'arrondir d'un nombre.
any() : permet de savoir si un élément est itérable ou pas. Elle s'applique sur les listes, les tuples et les dictionnaires.
all() : elle permet de déterminer si tous les éléments d'une séquence sont évalués comme true, si tous les éléments sont true elle renvoie true sinon elle renvoie false.
- conversions de types de variables : 
int(), str(), float(), type()
type() : permet de retourner le type de la variable
- conversions binaires :
bin(), oct(), hex()
- fonction : input()
- fonction : format()
- fonction : open()

La méthode `seek()` en Python est utilisée pour déplacer le curseur de lecture (ou d'écriture) d'un fichier. Elle permet de positionner le curseur à un emplacement spécifique dans le fichier, ce qui est utile lorsque vous souhaitez lire ou écrire à partir d'une position particulière dans un fichier. La méthode `seek()` prend un ou deux arguments :

```python
f.seek(offset, whence)
```

- `offset`: Il s'agit de la position dans le fichier vers laquelle vous souhaitez déplacer le curseur. L'argument `offset` peut être positif (pour avancer dans le fichier) ou négatif (pour reculer dans le fichier). Si `offset` est positif, le curseur avance de `offset` octets à partir de la position spécifiée par `whence`. Si `offset` est négatif, le curseur recule de `offset` octets à partir de la position spécifiée par `whence`.

- `whence` (facultatif) : Il s'agit du point de référence à partir duquel `offset` doit être appliqué. Il peut prendre l'une des valeurs suivantes :
  - `os.SEEK_SET` (ou 0) : Positionner le curseur à `offset` octets à partir du début du fichier.
  - `os.SEEK_CUR` (ou 1) : Positionner le curseur à `offset` octets par rapport à la position actuelle du curseur.
  - `os.SEEK_END` (ou 2) : Positionner le curseur à `offset` octets par rapport à la fin du fichier.

Voici quelques exemples d'utilisation de la méthode `seek()` :

```python
# Ouvrir un fichier en mode lecture
with open('mon_fichier.txt', 'r') as f:
    # Déplacer le curseur à la position 10 (10 octets depuis le début)
    f.seek(10)

    # Lire les données à partir de cette position
    data = f.read()
    print(data)
```

```python
# Ouvrir un fichier en mode lecture
with open('mon_fichier.txt', 'r') as f:
    # Déplacer le curseur à 10 octets avant la fin du fichier
    f.seek(-10, os.SEEK_END)

    # Lire les données à partir de cette position
    data = f.read()
    print(data)
```

La méthode `seek()` est utile lorsque vous devez accéder à des parties spécifiques d'un fichier, comme avancer ou reculer dans le fichier pour lire ou écrire des données à partir d'une position donnée.

La méthode `strip()` en Python est utilisée pour supprimer les caractères de début et de fin d'une chaîne de caractères (string). Par défaut, elle supprime les espaces (caractères d'espacement, comme les espaces, les tabulations et les sauts de ligne) du début et de la fin de la chaîne, mais vous pouvez également spécifier un ensemble de caractères personnalisé à supprimer.

Voici comment utiliser la méthode `strip()` :

```python
texte = "   Ceci est une chaîne avec des espaces.   "
resultat = texte.strip()
print(resultat)  # "Ceci est une chaîne avec des espaces."
```

Comme vous pouvez le voir, la méthode `strip()` a supprimé les espaces du début et de la fin de la chaîne `texte`.

Vous pouvez également spécifier un ensemble de caractères personnalisé à supprimer. Par exemple :

```python
texte = "??Ceci est une chaîne avec des points d'interrogation??"
resultat = texte.strip('?')
print(resultat)  # "Ceci est une chaîne avec des points d'interrogation"
```

Dans cet exemple, la méthode `strip('?')` a supprimé les points d'interrogation du début et de la fin de la chaîne.

La méthode `strip()` est souvent utilisée pour nettoyer et normaliser les chaînes de caractères en supprimant les espaces ou d'autres caractères non souhaités des bords d'une chaîne. Cela peut être utile lors de la manipulation de données lues à partir de fichiers ou d'entrées utilisateur pour s'assurer que les chaînes sont bien formatées.


Les modules en python
- import module
- import module as md
- from module import fonction