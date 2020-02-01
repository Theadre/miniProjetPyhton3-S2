from models.db import Db
from models.cours import Cours
from models.etudiant import Etudiant
from typing import List

class Note:

    def __init__(self, etudiant: Etudiant, cours: Cours, note: float):
        self.etudiant = etudiant
        self.cours = cours
        self.note = note

    def __repr__(self):
        return f"La note {self.note} est attribuée pour l'étudiant {self.etudiant} dans le cours {self.cours}"

    @staticmethod
    def afficher():
        list = Note.get()
        print(f'\n{len(list)} notes:')
        for model in list:
            print(model)

    @staticmethod
    def add(model) -> None:
        model.etudiant = model.etudiant.__dict__
        model.cours = model.cours.__dict__
        Db.dictionary.get('notes').append(model.__dict__)

    @staticmethod
    def get():
        notes: List[Note] = []

        for model in Db.dictionary.get('notes'):
            etudiant = Etudiant(**model['etudiant'])
            cours = Cours(**model['cours'])
            note = model['note']

            notes.append(Note(etudiant, cours, note))

        return notes

    @staticmethod
    def parEtudiant(etudiant: Etudiant):
        notes: List[Note] = []

        for model in Note.get():
            if model.etudiant.nom == etudiant.nom and model.etudiant.prenom == etudiant.prenom:
                notes.append(model)

        return notes

    @staticmethod
    def getParCoursTriee(cours: Cours):
        notes: List[Note] = []

        for model in Note.get():
            if model.cours.nom == cours.nom:
                notes.append(model)

        return sorted(notes, key=lambda e: e.note, reverse=True)

    @staticmethod
    def removeCours(cours: Cours):
        Db.dictionary['notes'] = [e for e in Db.dictionary['notes'] if e['cours']['nom'] != cours.nom]
        
        Cours.remove(cours)