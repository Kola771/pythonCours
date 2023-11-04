import re
from Conctat import Conctat


class main:
    def __init__(self):
        chemin = "myFiles.csv"
        while True:
            print("1- Ajouter un nouveau contact")
            print("2- Afficher tous les contacts")
            print("3- Mettre à jour un contact")
            print("4- Supprimer un contact")
            print("5- Quitter l'application")

            try:
                variable = int(input("Choisissez un nombre : "))
                if variable == 1:
                    nom = input("Entrez le nom de votre nouveau contact : ")
                    prenoms = input(
                        "Entrez le prénom de votre nouveau contact : ")
                    phone = input(
                        "Entrez le numéro de téléphone de votre nouveau contact : ")
                    adress = input("Entrez l'email du contact : ")
                    
                    # Modèle d'expression régulière pour valider une adresse e-mail
                    modele_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

                    # Utilisation de la fonction search pour trouver une correspondance dans la chaîne
                    correspondance = re.search(modele_email, adress)

                    # Si une correspondance est trouvée, l'e-mail est valide
                    if correspondance:
                        myContact = Conctat(nom, prenoms, phone, adress)
                        myContact.ajouter(chemin)
                    else:
                        print("L'adresse électronique renseigné n'est pas valide !!!")

                # Ajoutez les autres cases ici
                elif variable == 2:
                    myContact = Conctat()
                    myContact.afficher(chemin)
                elif variable == 3:
                    nomUp = input("Entrez le nom de votre nouveau contact : ")
                    prenomsUp = input(
                        "Entrez le prénom de votre nouveau contact : ")
                    phoneUp = input(
                        "Entrez le numéro de téléphone de votre nouveau contact : ")
                    adressUp = input("Entrez l'email du contact : ")
                    nom = input(
                        "Entrez le nom du contact dont il faut modifier les données : ")
                    prenoms = input(
                        "Entrez le prénom du contact dont il faut modifier les données : ")
                    
                    # Modèle d'expression régulière pour valider une adresse e-mail
                    modele_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

                    # Utilisation de la fonction search pour trouver une correspondance dans la chaîne
                    correspondance = re.search(modele_email, adressUp)

                    # Si une correspondance est trouvée, l'e-mail est valide
                    if correspondance:
                        myContact = Conctat(nomUp, prenomsUp, phoneUp, adressUp)
                        myContact.updateData(nom, prenoms, chemin)
                    else:
                        print("L'adresse électronique renseigné n'est pas valide !!!")
                elif variable == 4:
                    nom = input("Entrez le nom du contact à supprimer : ")
                    prenoms = input(
                        "Entrez le prénom du contact à supprimer : ")
                    myContact = Conctat(nom, prenoms)
                    myContact.deleteData(chemin)
                elif variable == 5:
                    print("Vous avez quitté l'application !!!")
                    break  # Quitter l'application
                else:
                    print("Option invalide")
            except ValueError:
                print("Vous n'avez pas entré un nombre !!!")


n = main()
