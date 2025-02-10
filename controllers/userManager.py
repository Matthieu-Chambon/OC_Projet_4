from models import User
from views import UserView

import json
import os
import re


class UserManager:
    def __init__(self):
        self.users = []
        self.userView = UserView()
        self.import_users_from_JSON()

    def import_users_from_JSON(self):
        fileName = "data/users.json"

        if os.path.exists(fileName):
            with open(fileName, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.users = [User(user["surname"], user["name"], user["dateOfBirth"], user["nationalID"]) for user in data]
            print("Importation des données réalisée avec succès !")
        else:
            print("Le fichier JSON n'existe pas. Aucune donnée importée.")

    def export_users_to_JSON(self):
        fileName = "data/users.json"
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def reset_scores(self):
        for user in self.users:
            user.score = 0

    def create_fake_users(self):
        self.users = []
        self.users.append(User("Dupont", "Jean", "15/04/1985", "AB12345"))
        self.users.append(User("Martin", "Sophie", "22/08/1990", "CD67890"))
        self.users.append(User("Durand", "Lucas", "05/12/1983", "EF13579"))
        self.users.append(User("Lefevre", "Emma", "30/06/1995", "GH24680"))
        self.users.append(User("Morel", "Hugo", "17/02/1988", "IJ98765"))
        self.users.append(User("Lemoine", "Alice", "09/09/1992", "KL54321"))
        self.users.append(User("Rousseau", "Thomas", "28/11/1980", "MN11223"))
        self.users.append(User("Perrin", "Camille", "14/07/1987", "OP33445"))
        self.users.append(User("Fournier", "Noé", "03/03/1993", "QR55667"))
        self.users.append(User("Girard", "Laura", "19/10/1991", "ST77889"))
        self.users.append(User("Blanc", "Maxime", "25/05/1986", "UV99001"))
        self.users.append(User("Gauthier", "Julie", "07/01/1994", "WX22334"))
        self.users.append(User("Chevalier", "Antoine", "12/06/1989", "YZ44556"))
        self.users.append(User("André", "Lucie", "08/04/1996", "AB66778"))
        self.users.append(User("Bernard", "Paul", "21/09/1984", "CD88990"))
        self.users.append(User("Noel", "Clara", "02/12/1982", "EF11223"))

    def create_new_user(self):
        print("\n - Creation d'un nouveau utilisateur -")

        # Choix du nom de famille
        regex = r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$"
        surname = ""
        while True:
            surname = input("\n>>> Entrez le nom de famille : ")

            if re.fullmatch(regex, surname):
                print(f"Nom de famille \"{surname}\" valide !")
                break
            else:
                print(f"Nom de famille \"{surname}\" invalide :(")

        # Choix du prénom
        regex = r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$"
        name = ""
        while True:
            name = input("\n>>> Entrez le prénom : ")

            if re.fullmatch(regex, name):
                print(f"Prénom \"{name}\" valide !")
                break
            else:
                print(f"Prénom \"{name}\" invalide :(")

        # Choix de la date de naissance
        regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        dateOfBirth = ""
        while True:
            dateOfBirth = input("\n>>> Entrez une date de naissance (au format JJ/MM/AAAA) : ")

            if re.fullmatch(regex, dateOfBirth):
                print(f"Date de naissance \"{dateOfBirth}\" valide !")
                break
            else:
                print(f"Date de naissance \"{dateOfBirth}\" invalide :(")

        # Choix de l'ID national
        regex = r"^[A-Z]{2}\d{5}$"
        nationalID = ""
        while True:
            nationalID = input("\n>>> Entrez votre identifiant national (au format AB12345) : ")

            if re.fullmatch(regex, nationalID):
                print(f"Identifiant national \"{nationalID}\" valide !")
                break
            else:
                print(f"Identifiant national \"{nationalID}\" invalide :(")

        self.users.append(User(
            surname,
            name,
            dateOfBirth,
            nationalID
        ))

        print("\nUtilisateur créé avec succès !")

        self.export_users_to_JSON()

    def display_users(self):
        self.userView.display_users(self.users)
