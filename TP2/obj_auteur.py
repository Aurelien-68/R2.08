from obj_couleur import Couleur

class Auteur(Couleur):
    nombre_total_auteurs=0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom
        self.prenom = prenom
        if pays == None:
            self.pays = "Inconnu"
        else:
            self.pays = pays
        if date_naissance == None:
            self.date_naissance = "Inconnue"
        else:
            self.date_naissance = date_naissance

    def __str__(self):
        return f"{Auteur.BLEU}{self.id}.\t: {Auteur.NO_COLOR}{self.prenom} {self.nom} {Auteur.MAGENTA}(né(e) le {self.date_naissance} en {self.pays}) {Auteur.NO_COLOR}"

if __name__=="__main__":
    print("Création de 3 instances de Auteur et affichage...")
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE","Jules","France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)
    print(bridou.pays)
    print(bridou.date_naissance)