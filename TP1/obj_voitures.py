class Voitures():
    prix_litre=1.70
    def __init__(self, marque="ferrari", modele="SF90_spider", annee=2010, prix = None, couleur="Blanc", conso=6.0) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix=prix
        self.couleur= couleur
        self.conso=conso
    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture:  {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso } L/100km {self.prix}"

    def calcul_consommation(self,distance):
        litres=(self.conso/100)*distance
        return f"Pour faire {distance} km la {self.modele} utilise {litres} L"

    def calcul_prix(self,distance):
        prix=self.prix_litre*Voitures.calcul_consommation(self,distance)
        return prix