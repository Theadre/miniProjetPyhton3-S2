class Etudiant():

    def __init__(self, prenomEtudiant, nomEtudiant, ageEtudiant):
        self.prenomEtudiant = prenomEtudiant
        self.nomEtudiant = nomEtudiant
        self.ageEtudiant = ageEtudiant

    def __setPrenomEtudiant(self, prenomEtudiant):
        self.__prenomEtudiant = prenomEtudiant

    def __getPrenomEtudiant(self):
        return self.__prenomEtudiant

    def __setNomEtudiant(self, nomEtudiant):
        self.__nomEtudiant = nomEtudiant

    def __getNomEtudiant(self):
        return self.__nomEtudiant


    def __setAgeEtudiant(self, ageEtudiant):
        self.__ageEtudiant= ageEtudiant

    def __getAgeEtudiant(self):
        return self.__ageEtudiant

