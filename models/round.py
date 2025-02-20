from models.match import Match

from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.matchsList = []
        self.startDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.endDate = "Aucune date de fin"

    def __str__(self):
        return (
            f"Name : {self.name}, "
            f"Start date : {self.startDate}, "
            f"End date : {self.endDate}, "
            f"Matchs : {self.matchsList}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "matchsList": [match.to_dict() for match in self.matchsList],
            "startDate": self.startDate,
            "endDate": self.endDate
        }

    @staticmethod
    def from_dict(round_dict):
        round = Round(round_dict["name"])
        round.startDate = round_dict["startDate"]
        round.endDate = round_dict["endDate"]
        round.matchsList = [
            Match.from_dict(match_dict)
            for match_dict in round_dict["matchsList"]]

        return round
