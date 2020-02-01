from models.db import Db
from typing import List

class Cours:

    def __init__(self, nom: str, annee: int):
        self.nom = nom
        self.annee = annee

    def __repr__(self) -> str :
        return f'{self.nom} ({self.annee})'

    @staticmethod
    def afficher() -> None:
        list = Cours.get()
        print(f'\n{len(list)} cours:')
        for model in list:
            print(model)

    @staticmethod
    def add(model) -> None:
        Db.dictionary.get('cours').append(model.__dict__)

    @staticmethod
    def get():
        return [Cours(**model) for model in Db.dictionary.get('cours')]

    @staticmethod
    def remove(model) -> None:
        Db.dictionary.get('cours').remove(model.__dict__)
