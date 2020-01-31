from models.db import Db
from models.cour import Cour
from models.etudiant import Etudiant
from models.note import Note
from typing import List


def main(msg):

    while True:
        print(msg)
        choix = int(input("Votre choix: "))

        if choix == 1:
            fileName = input("Entrez le nom du fichier: (defaut: data.json)")

            Db.load(fileName)
            Etudiant.afficher()
            Cour.afficher()
            Note.afficher()

        elif choix == 2:
            print('Ajouter un etudiant')
            print('--------------------')

            prenom = input("Prenom: ")
            nom = input("Nom: ")
            age = int(input("Age: "))

            e = Etudiant(nom, prenom, age)

            Etudiant.add(e)

        elif choix == 3:
            print('Ajouter une note')
            note = int(input("Note a attribuer: "))

            # get students
            print('Liset des etudiants')
            etudiants: List[Etudiant] = Etudiant.get()

            for i, e in enumerate(etudiants): print(f'{i + 1}. {e}')

            indexEtudiant = int(input('Votre choix: '))

            etudiantSelectionne = etudiants[indexEtudiant - 1]

            # get cours
            print('Liste des cours')
            cours: List[Cour] = Cour.get()

            for i, e in enumerate(cours): print(f'{i + 1}. {e}')

            indexCour = int(input('Votre choix: '))

            courSelectionne = cours[indexCour - 1]

            # instanciate new note object
            noteObj = Note(etudiantSelectionne, courSelectionne, note)

            print(noteObj)

            Note.add(noteObj)

        elif choix == 4:
            print("Afficher les notes d'un etudiant")

            print('Liste des etudiants')

            etudiants: List[Etudiant] = Etudiant.get()

            for i, e in enumerate(etudiants): print(f'{i + 1}. {e}')

            indexEtudiant = int(input('Votre choix: '))

            etudiantSelectionne = etudiants[indexEtudiant - 1]

            print(f"Notes de {etudiantSelectionne}")

            for e in Note.parEtudiant(
                etudiantSelectionne): print(f'{e.cour}: {e.note}')

        elif choix == 5:
            print("Afficher les notes triees d'un cours")

            cours = Cour.get()

            # print list of cours
            for i, e in enumerate(cours): print(f'{i + 1}. {e}')

            indexCour = int(input("Votre choix: "))

            cour = cours[indexCour - 1]

            print(f'Notes triees du cours {cour}')

            for e in Note.getParCourTriee(cour):
                print(f'{e.etudiant}: {e.note}')

        elif choix == 6:
            print("Supprimer un cours")
            print("----------------")

            cours = Cour.get()

            for i, e in enumerate(cours):
                print(f'{i + 1}. {e}')

            indexCour = int(input("Votre choix: "))

            cour = cours[indexCour - 1]

            Note.removeCour(cour)

            print(
                f'Le cours {cour} et les notes assocciees ont ete supprimees')

        elif choix == 7:
            print("Sauvegarder des donnees dans un fichier")
            print("----------------")
            fileName = input("Entrez le nom du fichier: (defaut: data.json)")

            Db.save(fileName)

            print("Les donnees ont ete sauvegardees")

        elif choix == 8:
                print('Ajouter un cour')
                print('--------------------')
                nom = input("Cour: ")
                annee = input("Annee: ")

                c = Cour(nom, annee)

                Cour.add(c)

        elif choix == 9:
            Etudiant.afficher()
            Cour.afficher()
            Note.afficher()

        else:
            quit()


# ******
msg = """
    1. Lecture des données depuis un fichier
    2. Ajouter un étudiant
    3. Ajouter une note
    4. Afficher les notes d'un etudiant
    5. Afficher les notes triees d'un cours
    6. Supprimer un cours
    7. Sauvegarde des donnees dans un fichier
    ****************************************
    8. Ajouter un cour
    9. Voire les donne en memoire
    10. Quitter
    """
main(msg)
