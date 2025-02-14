from datetime import datetime


class Tournament:
    def __init__(self, name, location, rounds, players, description):
        self.name = name
        self.location = location
        self.startDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.endDate = None
        self.numberOfRounds = rounds
        self.currentRound = 1
        self.roundsList = []
        self.playersList = players
        self.description = description
        self.status = "En cours"

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "numberOfRounds": self.numberOfRounds,
            "currentRound": self.currentRound,
            "roundsList": [round.to_dict() for round in self.roundsList],
            "playersList": [player.to_dict() for player in self.playersList],
            "description": self.description,
            "status": self.status
        }
