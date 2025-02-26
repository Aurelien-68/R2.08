class Voitures():
    # Constructeur avec 3 arguments...
    def __init__(self, marque="ferrari", modele="SF90_spider", annee=2010) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"



# Création d’une instance...
car = Voitures("Renault", "Clio", 2018)
# Lecture d’un attribut d’instance...
caisse = car.modele
# Affichage...
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
# Ecriture (modification) d’un attribut d’instance...
car.annee = 2020
# Affichage encore...
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")

print(car)

car2=Voitures("peugot", "205")
print(car2)

ma_voiture = Voitures("Bugatti", "Veyron")
print(ma_voiture)

car4=Voitures()
print(car4)

car5=Voitures( modele="F40")
print(car5)

voiture6 = Voitures(modele = "296_GTS")
print(voiture6)

#question 5 QCM
print(type(voiture6))
print(vars(voiture6))
print(dir(voiture6))
