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

