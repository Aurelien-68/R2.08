class Voitures():
    prix_litre=1.70
    def __init__(self ,marque="ferrari", modele="SF90_spider", annee=2010, prix = None, couleur="Blanc", conso=6.0, _id_series="A123 B456 C789", __audio_code="0000") :
        # Trois attributs d’instance...

        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix=prix
        self.couleur= couleur
        self.conso=conso
        self._id_series = _id_series
        self.__audio_code=__audio_code
    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture:  {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso } L/100km {self.prix}"

    def calcul_consommation(self,distance):
        return (self.conso/100)*distance

    def calcul_prix(self,dist):
        return self.prix_litre * Voitures.calcul_consommation(self,dist)

    def modif_prix_litre(self, prix):
        self.prix_litre=prix

    def calcul_co2(self,d):
        return Voitures.calcul_consommation(self,d) *2.3


