from models.db import Db
from models.cours import Cours
from models.etudiant import Etudiant
from models.note import Note
from typing import List


def main(msg):

    while True:
        print(msg)
        choix = int(input("Votre choix: "))

        if choix == 1:
            fileName = input("Entrez le nom du fichier: (défaut: data.txt)")

            Db.load(fileName)
            Etudiant.afficher()
            Cours.afficher()
            Note.afficher()

        elif choix == 2:
            print('Ajouter un étudiant')
            print('--------------------')

            prenom = input("Prénom: ")
            nom = input("Nom: ")
            age = int(input("Âge: "))

            e = Etudiant(nom, prenom, age)

            Etudiant.add(e)

        elif choix == 3:
            print('Ajouter une note')
            note = int(input("Note à attribuer: "))

            # get students
            print('Liste des étudiants')
            etudiants: List[Etudiant] = Etudiant.get()

            for i, e in enumerate(etudiants): print(f'{i + 1}. {e}')

            indexEtudiant = int(input('Votre choix: '))

            etudiantSelectionne = etudiants[indexEtudiant - 1]

            # get cours
            print('Liste des cours')
            cours: List[Cours] = Cours.get()

            for i, e in enumerate(cours): print(f'{i + 1}. {e}')

            indexCours = int(input('Votre choix: '))

            coursSelectionne = cours[indexCours - 1]

            # instanciate new note object
            noteObj = Note(etudiantSelectionne, coursSelectionne, note)

            print(noteObj)

            Note.add(noteObj)

        elif choix == 4:
            print("Afficher les notes d'un étudiant")

            print('Liste des étudiants')

            etudiants: List[Etudiant] = Etudiant.get()

            for i, e in enumerate(etudiants): print(f'{i + 1}. {e}')

            indexEtudiant = int(input('Votre choix: '))

            etudiantSelectionne = etudiants[indexEtudiant - 1]

            print(f"Notes de {etudiantSelectionne}")

            for e in Note.parEtudiant(
                etudiantSelectionne): print(f'{e.cours}: {e.note}')

        elif choix == 5:
            print("Afficher les notes triées d'un cours")

            cours = Cours.get()

            # print list of cours
            for i, e in enumerate(cours): print(f'{i + 1}. {e}')

            indexCours = int(input("Votre choix: "))

            cours = cours[indexCours - 1]

            print(f'Notes triées du cours {cours}')

            for e in Note.getParCoursTriee(cours):
                print(f'{e.etudiant}: {e.note}')

        elif choix == 6:
            print("Supprimer un cours")
            print("----------------")

            cours = Cours.get()

            for i, e in enumerate(cours):
                print(f'{i + 1}. {e}')

            indexCours = int(input("Votre choix: "))

            cours = cours[indexCours - 1]

            Note.removeCours(cours)

            print(
                f'Le cours {cours} et les notes assocciées ont été supprimées')

        elif choix == 7:
            print("Sauvegarder des données dans un fichier")
            print("----------------")
            fileName = input("Entrez le nom du fichier: (défaut: data.txt)")

            Db.save(fileName)

            print("Les données ont ete sauvegardées")

        elif choix == 8:
                print('Ajouter un cours')
                print('--------------------')
                nom = input("Cours: ")
                annee = input("Année: ")

                c = Cours(nom, annee)

                Cours.add(c)

        elif choix == 9:
            Etudiant.afficher()
            Cours.afficher()
            Note.afficher()

        else:
            quit()


# ******
msg = """
    1. Lecture des données depuis un fichier
    2. Ajouter un étudiant
    3. Ajouter une note
    4. Afficher les notes d'un étudiant
    5. Afficher les notes triées d'un cours
    6. Supprimer un cours
    7. Sauvegarde des données dans un fichier
    ****************************************
    8. Ajouter un cours
    9. Voir les données en mémoire
    10. Quitter
    """
main(msg)
