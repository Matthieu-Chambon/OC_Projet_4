from models import User
from views import UserView

# import re

from rich import print
from rich.rule import Rule


class UserManager:
    def __init__(self, app):
        self.users = User.load_users_from_JSON()
        self.userView = UserView()

        self.app = app

        self.regex_patterns = {
            "surname": r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$",
            "name": r"^[A-ZÀ-Ö][A-Za-zÀ-ÖØ-öø-ÿ' -]{2,50}$",
            "dateOfBirth": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$",
            "nationalID": r"^[A-Z]{2}\d{5}$"
        }

    def create_new_user(self):

        print()
        rule = Rule(title="Création d'un nouveau utilisateur", style="white")
        print(rule)

        fields = {
            "surname": ["Entrez le nom de famille", None],
            "name": ["Entrez le prénom", None],
            "dateOfBirth": ["Entrez la date de naissance", "JJ/MM/AAAA"],
            "nationalID": ["Entrez l'identifiant national", "ex: AB12345"]
        }

        user_data = {}

        for attr, (prompt, options) in fields.items():
            user_data[attr] = self.app.get_valid_input(
                prompt,
                options,
                self.regex_patterns[attr],
                None
            )

        new_user = User(**user_data)
        self.users.append(new_user)
        self.userView.display_new_user(new_user)

        self.sort_users("alphabetical")
        User.save_users_to_JSON(self.users)

    def edit_user(self):
        print()
        rule = Rule(title="Modification d'un utilisateur", style="white")
        print(rule)

        while True:
            self.display_users()
            user_input = self.app.get_valid_input(
                "Entrez le [red]numéro[/red] de l'utilisateur à modifier",
                "q > quitter",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q"
            )

            if user_input.lower() == "q":
                break

            user_index = int(user_input) - 1
            if user_index < len(self.users):
                user = self.users[user_index]

                fields = {
                    "1": ["surname", "le nom de famille"],
                    "2": ["name", "le prénom"],
                    "3": ["dateOfBirth", "la date de naissance"],
                    "4": ["nationalID", "l'identifiant national"]
                }

                while True:
                    self.userView.display_user(user)
                    field_input = self.app.get_valid_input(
                        "Entrez le [red]numéro[/red] du champ à modifier",
                        None,
                        r"^[1234qQ]$",
                        "q"
                    )

                    if field_input.lower() == "q":
                        break

                    if field_input in fields:
                        attr, label = fields[field_input]
                        new_value = self.app.get_valid_input(
                            f"Entrez {label}",
                            None,
                            self.regex_patterns[attr],
                            None
                        )
                        setattr(user, attr, new_value)
                        print("[green]L'utilisateur a été modifié avec succès")

                        self.sort_users("alphabetical")
                        User.save_users_to_JSON(self.users)

                    else:
                        print("[red]Choix invalide, veuillez réessayer.")

            else:
                print("[red]Choix invalide, veuillez réessayer.")

    def delete_user(self):
        self.display_users()
        while True:
            user_input = self.app.get_valid_input(
                "Entrez le numéro de l'utilisateur à supprimer",
                "q > quitter",
                r"^[1-9][0-9]*$|^[qQ]$",
                "q"
            )

            if user_input == "q" or user_input == "Q":
                break

            elif int(user_input) <= len(self.users):
                surname = self.users[int(user_input)-1].surname
                name = self.users[int(user_input)-1].name
                print(f"[red]Utilisateur {surname} {name} supprimé")
                self.users.pop(int(user_input)-1)
                self.display_users()
                User.save_users_to_JSON(self.users)

            else:
                print("[red]Le nombre choisi est trop grand. Réessayez.")

    def sort_users(self, order):
        if order == "alphabetical":
            self.users.sort(key=lambda user: user.surname, reverse=False)

    def display_users(self):
        self.userView.display_users(self.users)
