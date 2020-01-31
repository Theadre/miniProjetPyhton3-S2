class Cours():

    def __init__(self, nomCours):
        self.nomCours = nomCours

    def __setNomCours(self, nomCours):
        self.__nomCours = nomCours

    def __getNomCours(self):
        return self.__nomCours


