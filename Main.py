from Class.Etudiant import Etudiant
from Class.Cours import Cours
from Class.Note import Note
import platform
import os
import json


def main():

    choix = ""


    # Fonctions

    def Clean():
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")

    # Debut du programme


    print("""
    1. Lecture des données depuis un fichier
    2. Ajouter un étudiant
    3. Ajouter une note
    4. Afficher les notes d'un etudiant
    5. Afficher les notes triees d'un cours
    6. Supprimer un cours
    7. Sauvegarde des donnees dans un fichier
    8. Quitter""")

    choix = input("Votre choix :")

    #--------------------------------------------------
    # Choix 1 Lecture des données depuis un fichier
    if choix == "1":

        importFichier = input("Entrez le nom du fichier :")
        tableEtudiant = []
        tableCours = []
        tableNote = []
        data = ""
        i = 0
        f = 0
        e = 0

        # Chargement des etudiants
        with open(importFichier) as json_file:
            data = json.load(json_file)
            for item in data:
                if item['type'] == "etudiant":
                    Etudiant(item['prenom'], item['nom'], item['age'])
                    tableEtudiant.append(item['prenom'] + " "+ item['nom'] + " (" + item['age'] + ")")
                    i = i + 1

        # Chargement des cours
        with open(importFichier) as json_file:
            data = json.load(json_file)
            for item in data:
                 if item['type'] == "cours":
                    Cours(item['nom'])
                    tableCours.append(item['nom'])
                    f = f + 1               

        # Chargement des notes
        with open(importFichier) as json_file:
            data = json.load(json_file)
            for item in data:
                 if item['type'] == "note":
                    Note(item['nom'], item['cours'], item['note'])
                    tableNote.append("La note " + str(item['note']) + " est attribuée pour l étudiant ")
                    e = e + 1   

        print(i, "étudiants:")
        a = 0
        while a < i:
            print(tableEtudiant[a])
            a = a + 1 

        print(f, "Cours:")
        a = 0
        while a < f:
            print(tableCours[a])
            a = a + 1  

        print(e, "Notes :")
        a = 0
        while a < e:
            print(tableNote[a])
            a = a + 1        

    #--------------------------------------------------
    # Choix 2 Ajouter un étudiant

    if choix == "2":
        Clean()
        print("""
        Ajouter un etudiant
         ------------------""")
        prenomEtudiant = input("Prenom :")
        nomEtudiant = input("Nom :")
        ageEtudiant = input("Age :")

        Etudiant(i, prenomEtudiant, nomEtudiant, ageEtudiant)
        i = i + 1

    #--------------------------------------------------
    # Choix 3 Ajouter une note
    if choix == "3":
        print("votre choix 3")

    #--------------------------------------------------
    # Choix 4 Afficher les notes d'un etudiant
    if choix == 4:
        print("votre choix 4")

    #--------------------------------------------------
    # Choix 5 Afficher les notes triees d'un cours
    if choix == "5":
        print("votre choix 5")

    #--------------------------------------------------
    # Choix 6 Supprimer un cours
    if choix == "6":
        print("votre choix 6")

    #--------------------------------------------------
    # Choix 7 Sauvegarde des donnees dans un fichier
    if choix == "7":
        print("votre choix 7")

    #-------------------------------------------------------------------
    #Choix 8 Quitter
    if choix == "q":
    # Quitter le programme
        quit()

if __name__ == "__main__":
    main()