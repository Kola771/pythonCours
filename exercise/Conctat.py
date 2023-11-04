from ContactManager import ContactManager

# Classe en python


class Conctat:
    def __init__(self, nom=None, prenoms=None, phone=None, adress=None):
        self.nom = nom
        self.prenoms = prenoms
        self.phone = phone
        self.adress = adress

    def ajouter(self, chemin):
        listes = [self.nom, self.prenoms, self.phone, self.adress]
        ContactManager.addContact(listes, chemin)
        
    def afficher(self, chemin):
        ContactManager.selectData(chemin)
        
    def updateData(self, nom, prenoms, chemin):
        listes = [self.nom, self.prenoms, self.phone, self.adress]
        ContactManager.updateData(listes, nom, prenoms, chemin)
        
    def deleteData(self, chemin):
        ContactManager.deleteData([self.nom, self.prenoms], chemin)