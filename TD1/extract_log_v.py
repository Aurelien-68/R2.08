import sys
from pathlib import Path

# Vérification du nombre d'arguments
if len(sys.argv) < 3:
    print("usage : extract_log_v.py nom_fichier.log mot_cle [-v]")
    exit(1)

# Récupération des arguments
log_file = Path(sys.argv[1]).resolve()
mot_cle = sys.argv[2]
flag_verbose = False

# Vérification du troisième argument facultatif
if len(sys.argv) == 4:
    if sys.argv[3] != "-v":
        print("Erreur : Le troisième argument doit être '-v' pour le mode détaillé.")
        exit(1)
    flag_verbose = True

# Vérification de l'existence du fichier
if not log_file.exists():
    print("Erreur : Le fichier spécifié n'existe pas.")
    exit(1)

# Vérification que c'est bien un fichier
if not log_file.is_file():
    print("Erreur : Le chemin spécifié n'est pas un fichier.")
    exit(1)

# Vérification du mot-clé
valid_keywords = ["ERROR", "WARNING", "INFO"]
if mot_cle not in valid_keywords:
    print("Erreur : Le mot clé doit être ERROR, WARNING ou INFO.")
    exit(1)


# Lecture du fichier et comptage des lignes contenant le mot-clé
compteur = 0
with log_file.open("r", encoding="utf-8") as f:
    for ligne in f:
        if mot_cle in ligne:
            compteur += 1
            if flag_verbose:
                print(ligne.strip()) #affiche la ligne sans les tab et saut de ligne (/n et /r)

# Affichage du nombre de lignes trouvées
print(f"Le nombre de lignes contenant '{mot_cle}' est : {compteur}")
