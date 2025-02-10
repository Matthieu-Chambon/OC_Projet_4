class User:
    def __init__(self, surname, name, dateOfBirth, nationalID):
        self.surname = surname
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.nationalID = nationalID
        self.score = 0

    def to_dict(self):
        return {
            "surname": self.surname,
            "name": self.name,
            "dateOfBirth": self.dateOfBirth,
            "nationalID": self.nationalID
            }


if __name__ == "__main__":
    pass
