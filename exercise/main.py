import csv
from ContactManager import ContactManager
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
                    myContact = Conctat(nom, prenoms, phone, adress)
                    myContact.ajouter(chemin)
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
                    myContact = Conctat(nomUp, prenomsUp, phoneUp, adressUp)
                    myContact.updateData(nom, prenoms, chemin)
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
