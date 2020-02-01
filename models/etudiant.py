from models.db import Db
from typing import List

class Etudiant:

    def __init__(self, nom: str, prenom: str, age: int):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __repr__(self):
        return f'{self.nom} {self.prenom} ({self.age} ans)'

    @staticmethod
    def afficher():
        list = Etudiant.get()
        print(f'\n{len(list)} étudiants:')
        for model in list:
            print(model)

    @staticmethod
    def add(model) -> None:
        Db.dictionary.get('étudiants').append(model.__dict__)

    @staticmethod
    def remove(model) -> None:
        Db.dictionary.get('étudiants').remove(model.__dict__)

    @staticmethod
    def get():
        return [Etudiant(**model) for model in Db.dictionary.get('étudiants')]