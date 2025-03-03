import json
import os

FILE_NAME = "data/users.json"


class User:
    def __init__(self, surname, name, dateOfBirth, nationalID):
        self.surname = surname
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.nationalID = nationalID

    def __str__(self):
        return (
            f"{self.surname} {self.name} "
            f"({self.dateOfBirth}) {self.nationalID}"
        )

    def to_dict(self):
        return {
            "surname": self.surname,
            "name": self.name,
            "dateOfBirth": self.dateOfBirth,
            "nationalID": self.nationalID
        }

    @staticmethod
    def from_dict(user_dict):
        return User(
            user_dict["surname"],
            user_dict["name"],
            user_dict["dateOfBirth"],
            user_dict["nationalID"]
        )

    @staticmethod
    def load_users_from_JSON():
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                print(
                    f"Importation des données du fichier JSON \"{FILE_NAME}\"."
                    )
                return [User.from_dict(user) for user in data]
        else:
            print(
                f"Le fichier JSON \"{FILE_NAME}\" n'existe pas."
                f" Aucune donnée importée.")

            return []

    @staticmethod
    def save_users_to_JSON(users):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([user.to_dict() for user in users], file, indent=4)

    def __eq__(self, other):
        return self.nationalID == other.nationalID

    def __hash__(self):
        return hash(self.nationalID)
