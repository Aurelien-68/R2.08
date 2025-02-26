from obj_voitures import Voitures

captur=Voitures("Renault", "Captur_TCE_90ch",2018, 20000,"gris foncé",7.21 )
print(captur)

clio=Voitures("Renault","Clio_TCE_100ch", 2018, 17000, "blau nuit", 5.51)
print(clio)

cons_litre=clio.calcul_consommation(1060)
print(f"{cons_litre} L")

prix=clio.calcul_prix(1060)
print(f"{prix} €")

p=clio.modif_prix_litre(5)
print(clio.prix_litre)
print(captur.prix_litre)

co2= clio.calcul_co2(1060)
print(f"{co2} kg de CO2")


print(clio._id_series)
print(clio._Voitures__audio_code)