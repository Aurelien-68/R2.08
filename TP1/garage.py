from obj_voitures import Voitures

captur=Voitures("Renault", "Captur_TCE_90ch",2018, 20000,"gris foncé",7.21 )
print(captur)

clio=Voitures("Renault","Clio_TCE_100ch", 2018, 17000, "blau nuit", 5.51)
print(clio)

cons_litre=Voitures.calcul_consommation(clio,1060)
print(cons_litre)

prix=Voitures.prix_litre(clio,1060)
print(prix)