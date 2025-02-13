import csv
import sys
from pathlib import Path

if __name__=='__main__':
    if len(sys.argv)<5:
        print(f"il doit y avoir 4 argument après {sys.argv[0]}")
        print("Utilisation: python dbmoy.py nom_fichier.txt NOM Prenom note1 [note2]...")
        sys.exit(1)

    fichier=sys.argv[1]
    f_path= Path(fichier)
    f_path=f_path.resolve()
    nom=sys.argv[2].upper()
    prenom=sys.argv[3].capitalize()
    notes=sys.argv[4:]
    try:
        total=0.0
        for note in notes:
            total+=float(note)
        moyenne=total/len(notes)
    except ValueError:
        print("Erraur: Veuillez entrer des notes valides sous forme de nombres.")
        exit(1)
    try:
        with open(f_path, mode='a', newline="") as fichier_csv:
            writer=csv.writer(fichier_csv)
            writer.writerow([nom, prenom, round(moyenne,1)])
        print(f"Les notes de {prenom}{nom} ont été enregistrées dans {str(fichier)}")
    except Exception as e:
        print(f"Erreur:{e}")
