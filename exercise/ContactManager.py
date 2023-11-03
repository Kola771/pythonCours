import csv
import os

class ContactManager:
    # Fonction d'ajouts pour nouveau contact
    def addContact(listes, chemin):
        x = False
        with open('myFiles.csv', mode='r', newline='') as fichier_csv:
            reader = csv.reader(fichier_csv)
            donnees = list(reader)
        fichier_csv.close()
        if (all(listes)) :
            if len(donnees) > 1 :
                for el in range(1, len(donnees)):
                    # Convertir les chaînes de caractères en minuscules avant la comparaison
                    if [x.lower() for x in donnees[el][0:2]] == [x.lower() for x in listes[0:2]]:
                        x = True
                        break
                if x:
                    print ("Quelqu'un dans vos contacts possèdent déjà ce nom.")
                else :
                    donnees.append(listes)
                    with open(chemin, mode='w', newline='') as fichier_csv:
                        writer = csv.writer(fichier_csv)
                        
                        # Réécrivez l'en-tête en utilisant la première ligne de données
                        writer.writerow(donnees[0])

                        # Écrivez les données mises à jour sans l'en-tête
                        writer.writerows(donnees[1:])
                    fichier_csv.close()
                    print ("Données ajoutées avec succès.")
            else:
                donnees.append(listes)
                with open(chemin, mode='w', newline='') as fichier_csv:
                    writer = csv.writer(fichier_csv)
                    
                    # Réécrivez l'en-tête en utilisant la première ligne de données
                    writer.writerow(donnees[0])

                    # Écrivez les données mises à jour sans l'en-tête
                    writer.writerows(donnees[1:])
                fichier_csv.close()
                print ("Données ajoutées avec succès.")
        else :
            print ("Une des données que vous entrez est vide")
            
    # Fonction pour afficher tous les contacts
    def selectData(chemin):
        with open('myFiles.csv', mode='r', newline='') as fichier_csv:
            reader = csv.reader(fichier_csv)
            donnees = list(reader)
        fichier_csv.close()
        for el in range(1, len(donnees)):
            print(f'Nom: {donnees[el][0]}\nPrénoms: {donnees[el][1]}\nNuméro de téléphone: {donnees[el][2]}\nAdresse électronique: {donnees[el][3]}.')
            print('\n================================\n')
            
    # Fonction pour supprimer un contact
    def deleteData(liste, chemin):
        stock = False
        with open('myFiles.csv', mode='r', newline='') as fichier_csv:
            reader = csv.reader(fichier_csv)
            donnees = list(reader)
        fichier_csv.close()
        
        # Récupération de l'index de l'élément qu'on veut supprimer
        for index, el in enumerate(donnees):
            if index != 0:
                if [x.lower() for x in el[0:2]] == [x.lower() for x in liste[0:2]]:
                    stock = index
        
        # Création de ma nouvelle liste
        # Je ne stocke que les éléments dont l'index n'a pas la valeur de stock
        newData = [data for i, data in enumerate(donnees) if i != stock]
        
        with open(chemin, mode='w', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            
            # Réécrivez l'en-tête en utilisant la première ligne de données
            writer.writerow(newData[0])

            # Écrivez les données mises à jour sans l'en-tête
            writer.writerows(newData[1:])
        fichier_csv.close()  
        
    def updateData(listes, nom, prenoms, chemin):
        x = 0
        y = False
        with open('myFiles.csv', mode='r', newline='') as fichier_csv:
            reader = csv.reader(fichier_csv)
            donnees = list(reader)
        fichier_csv.close()
        if (all(listes)) :
            for el in range(1, len(donnees)):
                    # Convertir les chaînes de caractères en minuscules avant la comparaison
                    if [x.lower() for x in donnees[el][0:2]] == [x.lower() for x in listes[0:2]]:
                        x += 1
                        break
            if x == 0:
                y = True
            elif x == 1:
                y = True
            else :
                y = False
                
        else :
            print ("Une des données que vous entrez est vide")        