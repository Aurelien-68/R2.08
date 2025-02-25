import random
liste=[]
for i in range(random.randint(10,20)):
    liste.append((random.randint(0,100)))

while True:
    try:
        index=int(input("Donner un index: "))
        second_nb=float(input("Second nombre:"))
        print(f"valeur dans la liste: {liste[index]}")
        print(liste[index]/second_nb)
    except IndexError:
        print(f"Erreur: L'index {index} est en dehors de la liste([-{len(liste)};{len(liste)-1}])...")
    except ValueError:
        print(f"Erreur: La valeur saisie doit être un nombre...")
    except ZeroDivisionError:
        print(f"Erreur: Le second nombre ne doit pas être nul car il est au dénominateur...")
    except Exception as e:
        print(type(e))
