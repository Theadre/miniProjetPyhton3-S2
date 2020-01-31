from models.db import Db
from models.cour import Cour
from models.etudiant import Etudiant
from typing import List

class Note:

    def __init__(self, etudiant: Etudiant, cour: Cour, note: float):
        self.etudiant = etudiant
        self.cour = cour
        self.note = note

    def __repr__(self):
        return f"La note {self.note} est attribue pour l'étudiant {self.etudiant} dans le cours {self.cour}"

    @staticmethod
    def afficher():
        list = Note.get()
        print(f'\n{len(list)} notes:')
        for model in list:
            print(model)

    @staticmethod
    def add(model) -> None:
        model.etudiant = model.etudiant.__dict__
        model.cour = model.cour.__dict__
        Db.dictionary.get('notes').append(model.__dict__)

    @staticmethod
    def get():
        notes: List[Note] = []

        for model in Db.dictionary.get('notes'):
            etudiant = Etudiant(**model['etudiant'])
            cour = Cour(**model['cour'])
            note = model['note']

            notes.append(Note(etudiant, cour, note))

        return notes

    @staticmethod
    def parEtudiant(etudiant: Etudiant):
        notes: List[Note] = []

        for model in Note.get():
            if model.etudiant.nom == etudiant.nom and model.etudiant.prenom == etudiant.prenom:
                notes.append(model)

        return notes

    @staticmethod
    def getParCourTriee(cour: Cour):
        notes: List[Note] = []

        for model in Note.get():
            if model.cour.nom == cour.nom:
                notes.append(model)

        return sorted(notes, key=lambda e: e.note, reverse=True)

    @staticmethod
    def removeCour(cour: Cour):
        Db.dictionary['notes'] = [e for e in Db.dictionary['notes'] if e['cour']['nom'] != cour.nom]
        
        Cour.remove(cour)