class SerieTV:
    types_series = ["Policier", "Comédie", "Science-fiction", "Drame", "Thriller", "Fantastique", "Horreur", "Médicale","N/A"]
    VERT = "\033[32m"
    ROUGE = "\033[31m"
    BLEU = "\033[34m"
    NO_COLOR = "\033[0m"
    def __init__(self, nom, type_serie, episodes_par_saison, annee_premiere_diffusion=None,pays=None,terminee=False ):
        self.nom=nom
        self.types_serie=type_serie if type_serie in SerieTV.types_series else "N/A"
        self.__episodes_par_saison=episodes_par_saison
        self.__nombre_saisons=len(self.__episodes_par_saison)
        self.annee_premiere_diffusion=annee_premiere_diffusion
        self.pays=pays
        self.__terminee=terminee

    def __str__(self):
        return f"Serie {self.nom} - {self.types_serie} (démarée en {self.pays} en {self.annee_premiere_diffusion}) {SerieTV.ROUGE if self.__terminee else SerieTV.VERT} {f"{self.__nombre_saisons} saisons au total" if self.__terminee else f"Actuellement {self.__nombre_saisons} saisons"} {SerieTV.NO_COLOR}"

    def get_episodes_par_saison(self):
        return self.__episodes_par_saison
    def ajoute_saison(self, nb):
        if self.__terminee==False:
            self.__episodes_par_saison.append(nb)
            self.__nombre_saisons=len(self.__episodes_par_saison)
        else:
            print("Erreur: la serie est terminée!! Vous pouvez ajouter une saison que a une serie pas terminée")

    def cloture_serie(self):
        self.__terminee=True

    def get_nombre_saisons(self):
        return self.__nombre_saisons

    def calcule_nombre_total_episodes(self):
        tot_ep=0
        for i in range(len(self.__episodes_par_saison)):
            tot_ep=tot_ep+self.__episodes_par_saison[i]
        return tot_ep

if __name__ == "__main__":
    mando = SerieTV('The Mandalorian', 'Science-fiction', [8, 8, 8], 2019, 'USA')
    casa = SerieTV('La casa de papel', 'Polar', [9, 6, 8, 8, 10], 2017, 'Espagne', True)
    game = SerieTV('Game of Thrones', 'Fantastique', [10, 10, 10, 10, 10, 10, 7, 6], terminee = True)
    lbdl = SerieTV('Le Bureau des Légendes', 'Drame', [10, 10, 10, 10, 10], 2015, 'France', True)
    print(casa)
    print()
    print(mando)
    print(f"Nombre d'épisodes de '{mando.nom}' : {mando.get_episodes_par_saison()}")
    print(f"Ajout d'une saison de 12 épisodes à : '{mando.nom}'...")
    mando.ajoute_saison(12)
    print(f"Nombre d'épisodes de '{mando.nom}' : {mando.get_episodes_par_saison()}")

    print(f"\nOn cloture '{mando.nom}' !")
    mando.cloture_serie()
    print(mando)
    print(f"Tentative d'ajout d'une saison de 20 épisodes à : '{mando.nom}'...")
    mando.ajoute_saison(20)
    print(f"Nombre d'épisodes de '{mando.nom}' : {mando.get_episodes_par_saison()}")
    print()
    for element in [mando, casa, game, lbdl]:
        print(f"La série '{element.nom}' comprend {SerieTV.BLEU}{element.calcule_nombre_total_episodes()} {SerieTV.NO_COLOR} épisodes sur {SerieTV.ROUGE} {element.get_nombre_saisons()} {SerieTV.NO_COLOR} saisons.")