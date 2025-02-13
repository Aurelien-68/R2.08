import sys
from pathlib import Path
if __name__ == '__main__':
    if len(sys.argv)<2:
        print("--> usage : extract_log.py nom_fichier.log mot_cl")
