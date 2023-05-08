# l'orienté objet qui est un paradigme de programmation
class utilisateur():
    def __init__(self): # un constructeur
        print("je suis le constructeur! ")
        


# nous pouvons utiliser la classe utilisateur telle qu'elle est
# creer une instance de la classe utilisateur
franck = utilisateur() # je viens de creer un objet de la classe utilisateur

# une classe avec les attributs
class Personne:
    def __init__(self, c_nom, c_age):
        self.nom= c_nom
        self.age= c_age

# creer un objet personne 
personne1= Personne("franck", 36)
print(personne1.nom, personne1.age)
# on peux formater l'affichage
print(f"bonjour {personne1.nom} tu as {personne1.age} ans")
# nous pouvons creer plusieurs objet du type personnne
personne2 = Personne("fim", 25)
print(f"salut! {personne2.nom} tu as {personne2.age} ans")

# nous pouvons modifier le nom de l'objet personne1 par exemple
personne1.nom= "Vainqueur"
# affichons pour voir les modifications
print(f"bonjour {personne1.nom} tu as {personne1.age} ans")

# les variables de classe 
# on va creer une classe mafamille et nous aurons le premier enfant, deuxieme et etc

class MaFamille:
    id= 0 # c'est une variable de classe
    def __init__(self, c_nom, c_prenom, c_annais):
        self.nom = c_nom
        self.prenom = c_prenom
        self.annais= c_annais
        MaFamille.id +=1

enfant1= MaFamille("ilunga", "Fim", 2005)
print(f"je suis enfant n° :{MaFamille.id} je suis né en {enfant1.annais} , on m'appel {enfant1.nom} {enfant1.prenom}")
enfant2= MaFamille("Fim", "Vainqueur", 2003)
print(f"je suis enfant n° :{MaFamille.id} je suis né en {enfant2.annais} , on m'appel {enfant2.nom} {enfant2.prenom}")

# les methodes
# nous allons declarer une fonction se presenter
class MaFamille:
    id= 0 # c'est une variable de classe
    def __init__(self, c_nom, c_prenom, c_annais):
        self.nom = c_nom
        self.prenom = c_prenom
        self.annais= c_annais
        MaFamille.id +=1

    def salutation(self):# methode
        print(f"je suis l'enfant n°: {MaFamille.id} je suis né en {self.annais} on m'appel {self.nom} {self.prenom}")

# creer une instance (un objet)
fils1= MaFamille("Kabasele", "Achille", 2004)
# utiliser la methode salutation
fils1.salutation()