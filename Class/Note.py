class Note():

    def __init__(self, idEtudiant, idCours, note):
        self.idEtudiant = idEtudiant
        self.idCours = idCours
        self.note = note

    def __setIdEtudiant(self, idEtudiant):
        self.__idEtudiant = idEtudiant

    def __getIdEtudiant(self):
        return self.__idEtudiant


    def __setIdCours(self, idCours):
        self.__idCours = idCours

    def __getIdCours(self):
        return self.__idCours


    def __setNote(self, note):
        self.__note = note

    def __getNote(self):
        return self.__note

