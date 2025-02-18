from models import User
from views import UserView

import re


class UserManager:
    def __init__(self):
        self.users = User.load_users_from_JSON()
        self.userView = UserView()

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

        User.save_users_to_JSON(self.users)

    def create_new_user(self):

        print("\n - Creation d'un nouveau utilisateur -")

        regex_patterns = {
            "surname": r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$",
            "name": r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$",
            "dateOfBirth": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$",
            "nationalID": r"^[A-Z]{2}\d{5}$"
        }

        surname = self.get_valid_input("Entrez votre nom de famille", regex_patterns["surname"])
        name = self.get_valid_input("Entrez votre prénom", regex_patterns["name"])
        dateOfBirth = self.get_valid_input("Entrez votre date de naissance (JJ/MM/AAAA)", regex_patterns["dateOfBirth"])
        nationalID = self.get_valid_input("Entrez votre identifiant national (AB12345)", regex_patterns["nationalID"])

        self.users.append(User(
            surname,
            name,
            dateOfBirth,
            nationalID
        ))

        print("\n - Utilisateur enregistré avec succès - ")
        print(f"Nom de famille : {surname}")
        print(f"Prénom : {name}")
        print(f"Date de naissance : {dateOfBirth}")
        print(f"Identifiant national : {nationalID}")

        User.save_users_to_JSON(self.users)

    def get_valid_input(self, prompt, regex):
        while True:
            user_input = input(f"\n>>> {prompt} : ")

            if re.fullmatch(regex, user_input):
                return user_input
            else:
                print(f"\"{user_input}\" est invalide. Réessayez.")

    def display_users(self):
        self.userView.display_users(self.users)
